#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = ["requests", "beautifulsoup4", "markdownify"]
# ///
"""Mirror RadioHead Packet Radio library releases from airspayce.com to GitHub.

Each release becomes one commit ("RadioHead X.Y", dated on the release date) tagged vX.Y.
README.md is generated from the project home page with an automated-mirror notice.

Usage:
    ./update_mirror.py                 # publish the latest release if missing
    ./update_mirror.py --last 5        # publish the last 5 releases (oldest first)
    ./update_mirror.py --version 1.146 --dry-run

Auth: GH_TOKEN from the environment, or from .env next to this script.
"""

from __future__ import annotations

import argparse
import base64
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from requests.adapters import HTTPAdapter, Retry

UPSTREAM_URL = "https://www.airspayce.com/mikem/arduino/RadioHead/"
DEFAULT_REPO = "arimaker/radiohead-mirror"
KEEP = {".git", ".github"}
SCRIPT_DIR = Path(__file__).resolve().parent
BOT_NAME = "radiohead-mirror-bot"
BOT_EMAIL = "radiohead-mirror-bot@users.noreply.github.com"


@dataclass(frozen=True)
class Release:
    version: str
    date: str | None  # YYYY-MM-DD, from the revision history

    @property
    def tag(self) -> str:
        return f"v{self.version}"

    @property
    def zip_url(self) -> str:
        return f"{UPSTREAM_URL}RadioHead-{self.version}.zip"


def log(msg: str) -> None:
    print(f"==> {msg}", file=sys.stderr)


def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def version_key(v: str) -> tuple[int, ...]:
    return tuple(int(p) for p in v.split("."))


def http_session() -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = "radiohead-mirror-updater"
    s.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=1,
                                                      status_forcelist=[500, 502, 503, 504])))
    return s


def load_token() -> str | None:
    if token := os.environ.get("GH_TOKEN"):
        return token
    env = SCRIPT_DIR / ".env"
    if env.is_file():
        for line in env.read_text().splitlines():
            if line.startswith("GH_TOKEN="):
                return line.split("=", 1)[1].strip().strip("'\"") or None
    return None


class Git:
    """Runs git; the token is sent as an HTTP header so it never lands in .git/config."""

    def __init__(self, token: str | None):
        self.auth: list[str] = []
        if token:
            b64 = base64.b64encode(f"x-access-token:{token}".encode()).decode()
            self.auth = ["-c", "credential.helper=",
                         "-c", f"http.https://github.com/.extraheader=AUTHORIZATION: basic {b64}"]

    def __call__(self, *args: str, cwd: Path | None = None, env: dict | None = None,
                 capture: bool = False) -> str:
        res = subprocess.run(["git", *self.auth, *args], cwd=cwd, check=True, text=True,
                             env={**os.environ, **(env or {})},
                             stdout=subprocess.PIPE if capture else None)
        return (res.stdout or "").strip()


# --- upstream -----------------------------------------------------------------

def discover_releases(home_html: str) -> list[Release]:
    """All releases from the home page revision history, sorted by version."""
    found = {v: d for v, d in re.findall(r"(?m)^(?:<dd>)?\s*(\d+\.\d+) (\d{4}-\d{2}-\d{2})", home_html)}
    if not found:  # fall back to the download link
        found = {v: None for v in re.findall(r"RadioHead-(\d+(?:\.\d+)+)\.zip", home_html)}
    if not found:
        die(f"no releases found on {UPSTREAM_URL}")
    return [Release(v, found[v]) for v in sorted(found, key=version_key)]


def download_release(http: requests.Session, rel: Release, work: Path) -> Path:
    """Download and safely extract a release; returns the RadioHead/ source dir."""
    dl_dir = Path(tempfile.mkdtemp(prefix="dl-", dir=work))
    src_dir = Path(tempfile.mkdtemp(prefix="src-", dir=work))
    zip_path = dl_dir / f"RadioHead-{rel.version}.zip"
    log(f"Downloading {rel.zip_url}")
    with http.get(rel.zip_url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with zip_path.open("wb") as f:
            shutil.copyfileobj(r.raw, f)

    with zipfile.ZipFile(zip_path) as zf:
        if bad := zf.testzip():
            die(f"corrupt member in {zip_path.name}: {bad}")
        for name in zf.namelist():
            p = Path(name)
            if p.is_absolute() or ".." in p.parts:
                die(f"unsafe path in {zip_path.name}: {name}")
        zf.extractall(src_dir)

    src = src_dir / "RadioHead"
    if not (src / "RadioHead.h").is_file():
        die(f"unexpected archive layout in {zip_path.name} (no RadioHead/RadioHead.h)")
    props = src / "library.properties"
    if props.is_file():
        m = re.search(r"(?m)^version=(\S+)", props.read_text(errors="replace"))
        if m and m.group(1) != rel.version:
            log(f"warning: library.properties says {m.group(1)}, expected {rel.version}")
    return src


# --- README -------------------------------------------------------------------

def home_page_markdown(home_html: str) -> str:
    soup = BeautifulSoup(home_html, "html.parser")
    block = soup.select_one("div.textblock") or soup.select_one("div.contents")
    if block is None:
        die("could not find the documentation text on the home page")

    for tag in block.find_all(href=True):
        tag["href"] = urljoin(UPSTREAM_URL, tag["href"])
    for tag in block.find_all(src=True):
        tag["src"] = urljoin(UPSTREAM_URL, tag["src"])
    for tag in block.find_all(title=True):
        del tag["title"]
    for frag in block.select("div.fragment"):
        lines = [line.get_text() for line in frag.select("div.line")] or [frag.get_text()]
        pre = soup.new_tag("pre")
        code = soup.new_tag("code")
        code.string = "\n".join(lines)
        pre.append(code)
        frag.replace_with(pre)
    # Doxygen sections are <dl><dt>Title</dt><dd></dd></dl>: empty dd -> heading,
    # otherwise (e.g. the revision history) -> bold title + bullet list, since
    # GitHub doesn't render Markdown definition lists.
    for dl in block.find_all("dl"):
        title = dl.find("dt").get_text(strip=True) if dl.find("dt") else ""
        items = [dd for dd in dl.find_all("dd", recursive=False) if dd.get_text(strip=True)]
        if not items:
            h = soup.new_tag("h2")
            h.string = title
            dl.replace_with(h)
            continue
        wrap = soup.new_tag("div")
        p = soup.new_tag("p")
        strong = soup.new_tag("strong")
        strong.string = title
        p.append(strong)
        ul = soup.new_tag("ul")
        for dd in items:
            dd.name = "li"
            ul.append(dd.extract())
        wrap.extend([p, ul])
        dl.replace_with(wrap)

    md = markdownify(str(block), heading_style="ATX", bullets="-", code_language="",
                     newline_style="backslash")
    md = re.sub(r"[ \t]+\n", "\n", md)
    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def readme(rel: Release, body: str) -> str:
    released = f" (released {rel.date})" if rel.date else ""
    return f"""# RadioHead Packet Radio library (mirror)

> [!NOTE]
> **This is an automated, unofficial mirror** of the [RadioHead Packet Radio library]({UPSTREAM_URL})
> by Mike McCauley / AirSpayce Pty Ltd. It is not the official repository: please report issues and
> send patches upstream as described below.
>
> This commit contains **RadioHead {rel.version}**{released}, imported unmodified from
> <{rel.zip_url}>. Each release is a commit tagged `vX.Y`; the repository is updated
> automatically by a daily GitHub Actions workflow (`.github/workflows/update-mirror.yml`).
>
> RadioHead is dual licensed: GPL-3 (see `LICENSE` and the full text in `COPYING`) or a commercial
> license from AirSpayce. Only `README.md` and `COPYING` are added by this mirror.

The text below is the project home page at <{UPSTREAM_URL}>.

---

{body}"""


# --- mirror -------------------------------------------------------------------

def sync_tree(src: Path, repo: Path) -> None:
    for entry in repo.iterdir():
        if entry.name in KEEP:
            continue
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry)
        else:
            entry.unlink()
    shutil.copytree(src, repo, dirs_exist_ok=True, symlinks=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--last", type=int, default=1, metavar="N", help="publish the last N releases (default 1)")
    ap.add_argument("--version", action="append", default=[], metavar="X.Y", help="publish specific version(s)")
    ap.add_argument("--dry-run", action="store_true", help="do everything except push; keep the work dir")
    ap.add_argument("--force", action="store_true", help="re-publish versions whose tag already exists")
    ap.add_argument("--repo", default=os.environ.get("MIRROR_REPO", DEFAULT_REPO))
    ap.add_argument("--branch", default=os.environ.get("BRANCH", "main"))
    args = ap.parse_args()

    for cmd in ("git",):
        if not shutil.which(cmd):
            die(f"missing required command: {cmd}")
    token = load_token()
    if not token and not args.dry_run:
        die("GH_TOKEN not set (env or .env)")
    git = Git(token)
    http = http_session()

    log(f"Fetching {UPSTREAM_URL}")
    resp = http.get(UPSTREAM_URL, timeout=60)
    resp.raise_for_status()
    home_html = resp.text
    releases = discover_releases(home_html)
    if args.version:
        known = {r.version: r for r in releases}
        wanted = [known.get(v, Release(v, None)) for v in sorted(set(args.version), key=version_key)]
    else:
        wanted = releases[-args.last:]
    log("Requested: " + ", ".join(r.version for r in wanted))
    body = home_page_markdown(home_html)

    work = Path(tempfile.mkdtemp(prefix="radiohead-mirror-"))
    try:
        repo = work / "repo"
        git("clone", "--quiet", f"https://github.com/{args.repo}.git", str(repo))
        existing = set(git("tag", "--list", cwd=repo, capture=True).split())
        todo = [r for r in wanted if args.force or r.tag not in existing]
        if not todo:
            log("Mirror already has all requested versions, nothing to do")
            return
        has_branch = subprocess.run(["git", "rev-parse", "-q", "--verify", f"origin/{args.branch}"],
                                    cwd=repo, capture_output=True).returncode == 0
        git("checkout", "--quiet", "-B", args.branch, *([f"origin/{args.branch}"] if has_branch else []), cwd=repo)

        # Full GPL-3 text from the mirror's initial commit, kept as COPYING.
        gpl = None
        if has_branch:
            root = git("rev-list", "--max-parents=0", "HEAD", cwd=repo, capture=True).splitlines()[0]
            try:
                gpl = git("show", f"{root}:LICENSE", cwd=repo, capture=True) + "\n"
            except subprocess.CalledProcessError:
                pass
        if gpl is None and (repo / "COPYING").is_file():
            gpl = (repo / "COPYING").read_text()

        for rel in todo:
            src = download_release(http, rel, work)
            sync_tree(src, repo)
            if gpl:
                (repo / "COPYING").write_text(gpl)
            (repo / "README.md").write_text(readme(rel, body))

            git("add", "-A", cwd=repo)
            date = f"{rel.date}T12:00:00+00:00" if rel.date else datetime.now(UTC).isoformat()
            env = {"GIT_AUTHOR_NAME": BOT_NAME, "GIT_AUTHOR_EMAIL": BOT_EMAIL,
                   "GIT_COMMITTER_NAME": BOT_NAME, "GIT_COMMITTER_EMAIL": BOT_EMAIL,
                   "GIT_AUTHOR_DATE": date, "GIT_COMMITTER_DATE": date}
            if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=repo).returncode == 0:
                log(f"{rel.version}: no file changes, tagging current commit")
            else:
                git("commit", "--quiet", "-m", f"RadioHead {rel.version}",
                    "-m", f"Imported from {rel.zip_url}", cwd=repo, env=env)
            git("tag", "-f", "-a", rel.tag, "-m", f"RadioHead {rel.version}", cwd=repo, env=env)
            log(f"Committed RadioHead {rel.version} ({rel.tag})")

        tags = [f"refs/tags/{r.tag}" for r in todo]
        if args.dry_run:
            log(f"Dry run: would push {args.branch} and {', '.join(r.tag for r in todo)} to {args.repo}")
            git("--no-pager", "log", "--format=%h %ad %s%d", "--date=short", "-n", str(len(todo) + 1), cwd=repo)
            return
        git("push", "--quiet", "origin", args.branch, cwd=repo)
        git("push", "--quiet", *(["--force"] if args.force else []), "origin", *tags, cwd=repo)
        log(f"Published {', '.join(r.tag for r in todo)} to https://github.com/{args.repo}")
    finally:
        if args.dry_run:
            log(f"Work dir kept: {work}")
        else:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()

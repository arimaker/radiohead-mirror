# RadioHead Packet Radio library (mirror)

> [!NOTE]
> **This is an automated, unofficial mirror** of the [RadioHead Packet Radio library](https://www.airspayce.com/mikem/arduino/RadioHead/)
> by Mike McCauley / AirSpayce Pty Ltd. It is not the official repository: please report issues and
> send patches upstream as described below.
>
> This commit contains **RadioHead 1.145** (released 2026-01-05), imported unmodified from
> <https://www.airspayce.com/mikem/arduino/RadioHead/RadioHead-1.145.zip>. Each release is a commit tagged `vX.Y`; the repository is updated
> automatically by `update_mirror.py`.
>
> RadioHead is dual licensed: GPL-3 (see `LICENSE` and the full text in `COPYING`) or a commercial
> license from AirSpayce. Only `README.md` and `COPYING` are added by this mirror.

The text below is the project home page at <https://www.airspayce.com/mikem/arduino/RadioHead/>.

---

This is the RadioHead Packet Radio library for embedded microprocessors. It provides a complete object-oriented library for sending and receiving packetized messages via a variety of common data radios and other transports on a range of embedded microprocessors.

## Download

The version of the package that this documentation refers to can be downloaded from <https://www.airspayce.com/mikem/arduino/RadioHead/RadioHead-1.147.zip>

You can always find the latest version of this documentation at <https://www.airspayce.com/mikem/arduino/RadioHead>

You can also find online help and discussion at <https://groups.google.com/group/radiohead-arduino> Please use that group for all questions and discussions on this topic. Do not contact the author directly, unless it is to discuss commercial licensing. Before asking a question or reporting a bug, please read

- <https://en.wikipedia.org/wiki/Wikipedia:Reference_desk/How_to_ask_a_software_question>
- <https://www.catb.org/esr/faqs/smart-questions.html>
- <https://www.chiark.greenend.org.uk/~shgtatham/bugs.html>

Caution: Developing this type of software and using data radios successfully is challenging and requires a substantial knowledge base in software and radio and data transmission technologies and theory. It may not be an appropriate project for beginners. If you are a beginner, you will need to spend some time gaining knowledge in these areas first.

## Overview

RadioHead consists of 2 main sets of classes: Drivers and Managers.

- Drivers provide low level access to a range of different packet radios and other packetized message transports.
- Managers provide high level message sending and receiving facilities for a range of different requirements.

Every RadioHead program will have an instance of a Driver to provide access to the data radio or transport, and usually an instance of a Manager that uses that driver to send and receive messages for the application. The programmer is required to instantiate a Driver and a Manager, and to initialise the Manager. Thereafter the facilities of the Manager can be used to send and receive messages.

It is also possible to use a Driver on its own, without a Manager, although this only allows unaddressed, unreliable transport via the Driver's facilities.

In some specialised use cases, it is possible to instantiate more than one Driver and more than one Manager.

A range of different common embedded microprocessor platforms are supported, allowing your project to run on your choice of processor.

Example programs are included to show the main modes of use.

## Drivers

The following Drivers are provided:

- [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) Works with Hope-RF RF22B and RF23B based transceivers, and compatible chips and modules, including the RFM22B transceiver module such as hthis bare module: <https://www.sparkfun.com/products/10153> and this shield: <https://www.sparkfun.com/products/11018> and this board: <https://www.anarduino.com/miniwireless> and RF23BP modules such as: <https://www.anarduino.com/details.jsp?pid=130> Supports GFSK, FSK and OOK. Access to other chip features such as on-chip temperature measurement, analog-digital converter, transmitter power control etc is also provided.
- [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html) Works with Silicon Labs Si4460/4461/4463/4464 family of transceivers chip, and the equivalent HopeRF RF24/26/27 family of chips and the HopeRF RFM24W/26W/27W modules. Supports GFSK, FSK and OOK. Access to other chip features such as on-chip temperature measurement, analog-digital converter, transmitter power control etc is also provided.
- [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) Works with Hope-RF RF69B based radio modules, such as the RFM69 module, (as used on the excellent Moteino and Moteino-USB boards from LowPowerLab <https://lowpowerlab.com/moteino/> ) and compatible chips and modules such as RFM69W, RFM69HW, RFM69CW, RFM69HCW (Semtech SX1231, SX1231H). Also works with Anarduino MiniWireless -CW and -HW boards <https://www.anarduino.com/miniwireless/> including the marvellous high powered MinWireless-HW (with 20dBm output for excellent range). Supports GFSK, FSK.
- [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) Works with Nordic nRF24 based 2.4GHz radio modules, such as nRF24L01 and others. Also works with Hope-RF RFM73 and compatible devices (such as BK2423). nRF24L01 and RFM73 can interoperate with each other.
- [RH\_NRF905](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF905.html) Works with Nordic nRF905 based 433/868/915 MHz radio modules.
- [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html) Works with Nordic nRF51 compatible 2.4 GHz SoC/devices such as the nRF51822. Also works with Sparkfun nRF52832 breakout board, with Arduino 1.8.9 and Sparkfun nRF52 boards manager 0.2.3.
- [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) Works with Semtech SX1276/77/78/79, Modtronix inAir4 and inAir9, and HopeRF RFM95/96/97/98 and other similar LoRa capable radios. Supports Long Range (LoRa) with spread spectrum frequency hopping, large payloads etc. FSK/GFSK/OOK modes are not (yet) supported. Also works with the same chips on Linux using LoRa-file-ops Linux driver ioctls to transmit and receive RadioHead compatible messages. Requires a modified version of LoRa-file-ops driver to be installed, and a compatible radio to be connected appropriately: <https://github.com/starnight/LoRa/tree/file-ops> See the [RH\_LoRaFileOps](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__LoRaFileOps.html) class documentation for more information.
- [RH\_MRF89](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__MRF89.html) Works with Microchip MRF89XA and compatible transceivers. and modules such as MRF89XAM9A and MRF89XAM8A.
- [RH\_CC110](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__CC110.html) Works with Texas Instruments CC110L transceivers and compatible modules such as Anaren AIR BoosterPack 430BOOST-CC110L
- [RH\_E32](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__E32.html) Works with EBYTE E32-TTL-1W serial radio transceivers (and possibly other transceivers in the same family)
- [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) Works with a range of inexpensive ASK (amplitude shift keying) RF transceivers such as RX-B1 (also known as ST-RX04-ASK) receiver; TX-C1 transmitter and DR3100 transceiver; FS1000A/XY-MK-5V transceiver; HopeRF RFM83C / RFM85. Supports ASK (OOK).
- [RH\_ABZ](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ABZ.html) Works with EcoNode SmartTrap, Tlera Grasshopper and family. Almost any board equipped with a muRata cmwx1zzabz module should work. Tested with EcoNode SmartTrap, Arduino 1.8.9, GrumpyOldPizza Arduino Core for STM32L0. When building for EcoNode SmartTrap in Arduino IDE, select board type Grasshopper-L082CZ. This chip and GrumpyOldPizza Arduino Core for STM32L0 are now supported by PlatformIO: <https://docs.platformio.org/en/latest/platforms/ststm32.html#arduino-stm32l0-configuration-system>
- [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) Works with Semtech SX1261/2/8 LoRa capable transceivers and compatible, such as LLCCC68 Can be configured to automatically control any digital output pins required to control external RF switches or amplifiers. Tested with NiceRF LoRa1268-915 and Teensy 3.1. <https://www.nicerf.com/lora-module/915mhz-lora-module-lora1262.html> Tested with LLCC68 in Ra-01SC module and Teensy 3.1. Tested with Heltec Cube Cell HTCC-AB01 and Teensy 3.1.
- [RH\_STM32WLx](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__STM32WLx.html) Works with STM32WLE5xx and STM32WLE4xx family processors that include a SX1261/2 multi power amplifier transceiver. Automatically manages the dedicated SPI interface and interrupt, and the internal SPI slave select and reset pins to the radio. Examples provided. Requires the stm32duino package using these instructions: <https://community.st.com/t5/stm32-mcus/stm32-arduino-stm32duino-tutorial/ta-p/49649>
- [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) Works with RS232, RS422, RS485, RS488 and other point-to-point and multidropped serial connections, or with TTL serial UARTs such as those on Arduino and many other processors, or with data radios with a serial port interface. [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) provides packetization and error detection over any hardware or virtual serial connection. Also builds and runs on Linux and OSX.
- [RH\_TCP](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__TCP.html) For use with simulated sketches compiled and running on Linux. Works with tools/etherSimulator.pl to pass messages between simulated sketches, allowing testing of Manager classes on Linux and without need for real radios or other transport hardware.
- [RHEncryptedDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHEncryptedDriver.html) Adds encryption and decryption to any RadioHead transport driver, using any encrpytion cipher supported by ArduinoLibs Cryptographic Library <https://rweather.github.io/arduinolibs/crypto.html> which also supports the newly adopted ASCON lightweight cryptography standard for IoT, as announced by National Institute of Standards and Technology (NIST).

Drivers can be used on their own to provide unaddressed, unreliable datagrams. All drivers have the same identical API. Or you can use any Driver with any of the Managers described below.

We welcome contributions of well tested and well documented code to support other transports.

If your radio or transciever is not on the list above, there is a good chance it won't work without modifying RadioHead to suit it. If you wish for support for another radio or transciever, and you send at least 2 of them to AirSpayce Pty Ltd, we will consider adding support for it.

## Managers

The drivers above all provide for unaddressed, unreliable (ie unacknowleged), variable length messages, but if you need more than that, the following Managers are provided:

- [RHDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHDatagram.html) Addressed, unreliable variable length messages, with optional broadcast facilities.
- [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) Addressed, reliable, retransmitted, acknowledged variable length messages.
- [RHRouter](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html) Multi-hop delivery of RHReliableDatagrams from source node to destination node via 0 or more intermediate nodes, with manual, pre-programmed routing.
- [RHMesh](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html) Multi-hop delivery of RHReliableDatagrams with automatic route discovery and rediscovery.

Any Manager may be used with any Driver.

## Platforms

A range of processors and platforms are supported:

- Arduino and the Arduino IDE (version 1.0 to 1.8.1 and 2.1.1 and later) Including Diecimila, Uno, Mega, Leonardo, Yun, Due, Zero, Minima and possibly others from <https://arduino.cc/>, Also similar boards such as
  - Moteino <https://lowpowerlab.com/moteino/>
  - Anarduino Mini <https://www.anarduino.com/mini/>
  - RedBearLab Blend V1.0 <https://redbearlab.com/blend/> (with Arduino 1.0.5 and RedBearLab Blend Add-On version 20140701)
  - MoteinoMEGA <https://lowpowerlab.com/shop/moteinomega> (with Arduino 1.0.5 and the MoteinoMEGA Arduino Core <https://github.com/LowPowerLab/Moteino/tree/master/MEGA/Core>)
  - ESP8266 on Arduino IDE and Boards Manager per <https://github.com/esp8266/Arduino> Tested using Arduino 1.6.8 with esp8266 by ESP8266 Community version 2.1.0 Also Arduino 1.8.1 with esp8266 by SparkFun Electronics 2.5.2 Examples serial\_reliable\_datagram\_\* and ask\_\* are shown to work. CAUTION: The GHz radio included in the ESP8266 is not yet supported. CAUTION: tests here show that when powered by an FTDI USB-Serial converter, the ESP8266 can draw so much power when transmitting on its GHz WiFi that VCC will sag causing random crashes. We strongly recommend a large cap, say 1000uF 10V on VCC if you are also using the WiFi.
  - Various Talk2 Whisper boards eg <https://wisen.com.au/store/products/whisper-node-lora>. Use Arduino Board Manager to install the Talk2 code support.
  - etc.
- STM32 F4 Discover board, using Arduino 1.8.2 or later and Roger Clarkes Arduino\_STM from <https://github.com/rogerclarkmelbourne/Arduino_STM32> Caution: with this library and board, sending text to Serial causes the board to hang in mysterious ways. Serial2 emits to PA2. The default SPI pins are SCK: PB3, MOSI PB5, MISO PB4. We tested with PB0 as slave select and PB1 as interrupt pin for various radios. [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) and [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) also work. Also works with stm32duino 1.8.0 from <https://github.com/stm32duino/Arduino_Core_STM32>, wich can be installed on Arduino with BoardManager. Select board: STM32 Discovery F407.
- ChipKIT Core with Arduino IDE on any ChipKIT Core supported Digilent processor (tested on Uno32) <https://chipkit.net/wiki/index.php?title=ChipKIT_core>
- Maple and Flymaple boards with libmaple and the Maple-IDE development environment <https://leaflabs.com/devices/maple/> and <https://www.open-drone.org/flymaple>
- Teensy including Teensy 3.1 and earlier built using Arduino IDE 1.0.5 to 1.6.4 and later with teensyduino addon 1.18 to 1.23 and later. <https://www.pjrc.com/teensy>
- Particle Photon <https://store.particle.io/collections/photon> and ARM3 based CPU with built-in Wi-Fi transceiver and extensive IoT software suport. RadioHead does not support the built-in transceiver but can be used to control other SPI based radios, Serial ports etc. See below for details on how to build RadioHead for Photon
- ATTiny built using Arduino IDE 1.8 and the ATTiny core from <https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json> using the instructions at <https://medium.com/jungletronics/attiny85-easy-flashing-through-arduino-b5f896c48189> (Caution: these are very small processors and not all RadioHead features may be available, depending on memory requirements) (Caution: we have not had good success building [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) sketches for ATTiny 85 with SpenceKonde ATTinyCore)
- ATtiny Mega (tinyAVR 1-series) chips supported by Spencer Konde's megaTinyCore (<https://github.com/SpenceKonde/megaTinyCore>) (on Arduino 1.8.9 or later) such as AtTiny 3216, ATtiny 1616 etc. These chips can be easily programmed through their UPDI pin, using an ordinary Arduino board programmed as a jtag2updi programmer as described in <https://github.com/SpenceKonde/megaTinyCore/blob/master/MakeUPDIProgrammer.md>. Make sure you set the programmer type to jtag2updi in the Arduino Tools->Programmer menu. See <https://github.com/SpenceKonde/megaTinyCore/blob/master/megaavr/extras/ImportantInfo.md> for links to pinouts and pin numbering information for all the suported chips.
- nRF51 compatible Arm chips such as nRF51822 with Arduino 1.6.4 and later using the procedures in <https://redbearlab.com/getting-started-nrf51822/>
- nRF52 compatible Arm chips such as as Adafruit BLE Feather board <https://www.adafruit.com/product/3406>
- Adafruit Feather. These are excellent boards that are available with a variety of radios. We tested with the Feather 32u4 with RFM69HCW radio, with Arduino IDE 1.6.8 and the Adafruit AVR Boards board manager version 1.6.10. <https://www.adafruit.com/products/3076>
- Adafruit Feather M0 boards with Arduino 1.8.1 and later, using the Arduino and Adafruit SAMD board support. <https://learn.adafruit.com/adafruit-feather-m0-basic-proto/using-with-arduino-ide>
- ESP32 built using Arduino IDE 1.8.9 or later using the ESP32 toolchain installed per <https://github.com/espressif/arduino-esp32> or from the Arduino IDE Board Manager. Tested up to version 3.0.2. The internal 2.4GHz radio is not yet supported. Tested with RFM22 using SPI interface. Uses the VSPI SPI bus by default. You can enable use of the alternative HSPI bus for SPI by defining RH\_ESP32\_USE\_HSPI in [RadioHead.h](https://www.airspayce.com/mikem/arduino/RadioHead/RadioHead_8h_source.html).
- Raspberry Pi Uses BCM2835 library for GPIO <https://www.airspayce.com/mikem/bcm2835/> Currently works only with [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) driver or other drivers that do not require interrupt support. Contributed by Mike Poublon.
- Linux and OSX Using the RHutil/HardwareSerial class, the [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) driver and any manager will build and run on Linux and OSX. These can be used to build programs that talk securely and reliably to Arduino and other processors or to other Linux or OSX hosts on a reliable, error detected (and possibly encrypted) datagram protocol over various types of serial line.
- Mongoose OS, courtesy Paul Austen. Mongoose OSis an Internet of Things Firmware Development Framework available under Apache License Version 2.0. It supports low power, connected microcontrollers such as: ESP32, ESP8266, TI CC3200, TI CC3220, STM32. <https://mongoose-os.com/>
- muRata cmwx1zzabz module, which includes an STM32L0 processor, a SX1276 LoRa radio and an antenna switch.
- Raspberry Pi Pico, on Arduino, using either the Raspberry Pi Pico/RP2040 core by Earle F. Philhower, version 1.93, installed per <https://arduino-pico.readthedocs.io/_/downloads/en/latest/pdf/> or the alternative Arduino MBED OS RP2040 core version 2.4.1. At this stage support is partial: [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) works but radio drivers that use interrupts do not (yet) work in either core.
- Heltec Cube Cell family, eg HTCC-AB01: <https://heltec.org/project/htcc-ab01-v2/> <https://resource.heltec.cn/download/CubeCell/HTCC-AB01/HTCC-AB01_SchematicDiagram.pdf> These modules have an ASR6501 or ASR6502 ARM Cortex M0+ processor <https://www.microchip.ua/wireless/ASR6501.pdf> which includes a built-in LoRa capable SX1262 radio, and which is supported by the RadioHead [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) driver. Demonstrated interoperation with [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) driver. Build with the CubeCell board support 1.5.0 via the Arduino Board Manager per <https://docs.heltec.org/en/node/asr650x/asr650x_general_docs/quick_start/cubecell-use-arduino-board-manager.html> Tested with 1.5.0 in Arduino IDE. [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) driver works with this board, but since the timer interrupt takes the timeout in milliseconds, not microseconds, the fastest bit rate we can support is 1000 / 8 = 125 bits per second.

Other platforms are partially supported, such as Generic AVR 8 bit processors, MSP430. We welcome contributions that will expand the range of supported platforms.

If your processor is not on the list above, there is a good chance it wont work without modifying RadioHead to suit it. If you wish for support for another processor, and you send 2 of them to AirSpayce Pty Ltd, we will consider adding support for it.

RadioHead is available (through the efforts of others) for PlatformIO. PlatformIO is a cross-platform code builder and the missing library manager. <https://platformio.org/#!/lib/show/124/RadioHead>

## History

RadioHead was created in April 2014, substantially based on code from some of our other earlier Radio libraries:

- [RHMesh](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html), [RHRouter](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html), [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) and [RHDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHDatagram.html) are derived from the RF22 library version 1.39.
- [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) is derived from the RF22 library version 1.39.
- [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) is derived from the RF69 library version 1.2.
- [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) is based on the VirtualWire library version 1.26, after significant conversion to C++.
- [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) was new.
- [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) is based on the NRF24 library version 1.12, with some significant changes.

During this combination and redevelopment, we have tried to retain all the processor dependencies and support from the libraries that were contributed by other people. However not all platforms can be tested by us, so if you find that support from some platform has not been successfully migrated, please feel free to fix it and send us a patch.

Users of [RHMesh](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html), [RHRouter](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html), [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) and [RHDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHDatagram.html) in the previous RF22 library will find that their existing code will run mostly without modification. See the [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) documentation for more details.

## Installation

For Arduino IDE, install in the usual way: unzip the distribution zip file to the libraries sub-folder of your sketchbook. The example sketches will be visible in in your Arduino, mpide, maple-ide or whatever. <https://arduino.cc/en/Guide/Libraries>

## Building for Particle Photon

The Photon is not supported by the Arduino IDE, so it takes a little effort to set up a build environment. Heres what we did to enable building of RadioHead example sketches on Linux, but there are other ways to skin this cat. Basic reference for getting started is: <https://particle-firmware.readthedocs.org/en/develop/build/>

- Download the ARM gcc cross compiler binaries and unpack it in a suitable place:

  ```
  cd /tmp
  wget https://launchpad.net/gcc-arm-embedded/5.0/5-2015-q4-major/+download/gcc-arm-none-eabi-5_2-2015q4-20151219-linux.tar.bz2
  tar xvf gcc-arm-none-eabi-5_2-2015q4-20151219-linux.tar.bz2
  ```
- If dfu-util and friends not installed on your platform, download dfu-util and friends to somewhere in your path

  ```
  cd ~/bin
  wget https://dfu-util.sourceforge.net/releases/dfu-util-0.8-binaries/linux-i386/dfu-util
  wget https://dfu-util.sourceforge.net/releases/dfu-util-0.8-binaries/linux-i386/dfu-suffix
  wget https://dfu-util.sourceforge.net/releases/dfu-util-0.8-binaries/linux-i386/dfu-prefix
  ```
- Download the Particle firmware (contains headers and libraries require to compile Photon sketches) to a suitable place:

  ```
  cd /tmp
  wget https://github.com/spark/firmware/archive/develop.zip
  unzip develop.zip
  ```
- Make a working area containing the RadioHead library source code and your RadioHead sketch. You must rename the sketch from .pde or .ino to application.cpp

  ```
  cd /tmp
  mkdir RadioHead
  cd RadioHead
  cp /usr/local/projects/arduino/libraries/RadioHead/ *.h .
  cp /usr/local/projects/arduino/libraries/RadioHead/ *.cpp .
  cp /usr/local/projects/arduino/libraries/RadioHead/examples/cc110/cc110_client/cc110_client.pde application.cpp
  ```
- Edit application.cpp and comment out any #include <SPI.h> so it looks like:

  ```
  // #include <SPI.h>
  ```
- Connect your Photon by USB. Put it in DFU mode as descibed in Photon documentation. Light should be flashing yellow
- Compile the RadioHead sketch and install it as the user program (this does not update the rest of the Photon firmware, just the user part:

  ```
  cd /tmp/firmware-develop/main
  PATH=$PATH:/tmp/gcc-arm-none-eabi-5_2-2015q4/bin make APPDIR=/tmp/RadioHead all PLATFORM=photon program-dfu
  ```
- You should see RadioHead compile without errors and download the finished sketch into the Photon.

## Compatible Hardware Suppliers

We have had good experiences with the following suppliers of RadioHead compatible hardware:

- LittleBird <https://littlebirdelectronics.com.au> in Australia for all manner of Arduinos and radios.
- LowPowerLab <https://lowpowerlab.com/moteino> in USA for the excellent Moteino and Moteino-USB boards which include Hope-RF RF69B radios on-board.
- Anarduino and HopeRF USA (<https://www.hoperfusa.com> and <https://www.anarduino.com>) who have a wide range of HopeRF radios and Arduino integrated modules.
- SparkFun <https://www.sparkfun.com/> in USA who design and sell a wide range of Arduinos and radio modules.
- Wisen <https://wisen.com.au> who design and sell a wide range of integrated radio/processor modules including the excellent Talk2 range.

## Coding Style

RadioHead is designed so it can run on small processors with very limited resources and strict timing contraints. As a result, we tend only to use the simplest and least demanding (in terms of memory and CPU) C++ facilities. In particular we avoid as much as possible dynamic memory allocation, and the use of complex objects like C++ strings, IO and buffers. We are happy with this, but we are aware that some people may think we are leaving useful tools on the table. You should not use this code as an example of how to do generalised C++ programming on well resourced processors.

## Code Contributions

We welcome, and will consider for merging into the mainline, contributions of fixes, patches, improvements etc. that meet the following criteria:

- Are generally useful to more than a few people.
- Are thoroughly tested.
- Dont break anything else.
- Are backwards compatible.
- Are properly and completely documented.
- Conform to the coding style of the rest of the library.
- Clearly transfer the ownership of the intellectual property to Mike McCauley.
- Are posted on the Google group as a patch in unified Diff format, made against the latest version of the library, downloaded from airspayce.com, as described above.

There is currently no known fully up-to-date git repository, and at present we have no intentions of making one ourselves.

## Donations

This library is offered under a free GPL license for those who want to use it that way. We try hard to keep it up to date, fix bugs and to provide free support. If this library has helped you save time or money, please consider donating at <https://www.airspayce.com> or here:

![](https://www.paypalobjects.com/en_AU/i/scr/pixel.gif)

[Passing Sensor Data Between RadioHead nodes](https://www.airspayce.com/mikem/arduino/RadioHead/packingdata.html)

## Trademarks

RadioHead is a trademark of AirSpayce Pty Ltd. The RadioHead mark was first used on April 12 2014 for international trade, and is used only in relation to data communications hardware and software and related services. It is not to be confused with any other similar marks covering other goods and services.

## Copyright

This software is Copyright (C) 2011-2022 Mike McCauley. Use is subject to license conditions. The main licensing options available are GPL V3 or Commercial:

## Open Source Licensing GPL V3

This is the appropriate option if you want to share the source code of your application with everyone you distribute it to, and you also want to give them the right to share who uses it. If you wish to use this software under Open Source Licensing, you must contribute all your source code to the open source community in accordance with the GPL Version 3 when your application is distributed. See <https://www.gnu.org/licenses/gpl-3.0.html>

## Commercial Licensing

This is the appropriate option if you are creating proprietary applications and you are not prepared to distribute and share the source code of your application. To purchase a commercial license, contact [info@.nosp@m.airs.nosp@m.payce.nosp@m..com](https://www.airspayce.com/mikem/arduino/RadioHead/#)

## Revision History

**Version**

- 1.1 2014-04-14\
  Initial public release
- 1.2 2014-04-23\
  Fixed various typos. \
  Added links to compatible Anarduino products.\
  Added [RHNRFSPIDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHNRFSPIDriver.html), [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) classes to support Nordic NRF24 based radios.
- 1.3 2014-04-28\
  Various documentation fixups.\
  [RHDatagram::setThisAddress()](https://www.airspayce.com/mikem/arduino/RadioHead/classRHDatagram.html#a2031c32443b797b275245344c8a36ef1) did not set the local copy of thisAddress. Reported by Steve Childress.\
  Fixed a problem on Teensy with RF22 and RF69, where the interrupt pin needs to be set for input, \
  else pin interrupt doesn't work properly. Reported by Steve Childress and patched by Adrien van den Bossche. Thanks.\
  Fixed a problem that prevented RF22 honouring setPromiscuous(true). Reported by Steve Childress.\
  Updated documentation to clarify some issues to do with maximum message lengths reported by Steve Childress.\
  Added support for yield() on systems that support it (currently Arduino 1.5.5 and later) so that spin-loops can suport multitasking. Suggested by Steve Childress.\
  Added [RH\_RF22::setGpioReversed()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html#a92281087776d50cdb1b0ce90c1d79165) so the reversal it can be configured at run-time after radio initialisation. It must now be called *after* init(). Suggested by Steve Childress.\
- 1.4 2014-04-29\
  Fixed further problems with Teensy compatibility for [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html). Tested on Teensy 3.1. The example/rf22\_\* examples now run out of the box with the wiring connections as documented for Teensy in [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html).\
  Added YIELDs to spin-loops in [RHRouter](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html), [RHMesh](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html) and [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html), [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html).\
  Tested [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) examples with Teensy 3.1: they now run out of the box.\
  Tested [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) examples with Teensy 3.1: they now run out of the box.\
  Reduced default SPI speed for NRF24 from 8MHz to 1MHz on Teensy, to improve reliability when poor wiring is in use.\
  on some devices such as Teensy.\
  Tested [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) examples with Teensy 3.1: they now run out of the box.\
- 1.5 2014-04-29\
  Added support for Nordic Semiconductor nRF905 transceiver with [RH\_NRF905](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF905.html) driver. Also added examples for nRF905 and tested on Teensy 3.1
- 1.6 2014-04-30\
  NRF905 examples were missing
- 1.7 2014-05-03\
  Added support for Arduino Due. Tested with [RH\_NRF905](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF905.html), [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html), [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html). IMPORTANT CHANGE to interrupt pins on Arduino with [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) and [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) constructors: previously, you had to specify the interrupt *number* not the interrupt *pin*. Arduinos and Uno32 are now consistent with all other platforms: you must specify the interrupt pin number. Default changed to pin 2 (a common choice with RF22 shields). Removed examples/maple/maple\_rf22\_reliable\_datagram\_client and examples/maple/maple\_rf22\_reliable\_datagram\_client since the rf22 examples now work out of the box with Flymaple. Removed examples/uno32/uno32\_rf22\_reliable\_datagram\_client and examples/uno32/uno32\_rf22\_reliable\_datagram\_client since the rf22 examples now work out of the box with ChipKit Uno32.
- 1.8 2014-05-08 \
  Added support for YIELD in Teensy 2 and 3, suggested by Steve Childress.\
  Documentation updates. Clarify use of headers and Flags\
  Fixed misalignment in [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) between ModemConfigChoice definitions and the implemented choices which meant you didnt get the choice you thought and GFSK\_Rb55555Fd50 hung the transmitter.\
  Preliminary work on Linux simulator.
- 1.9 2014-05-14 \
  Added support for using Timer 2 instead of Timer 1 on Arduino in [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) when RH\_ASK\_ARDUINO\_USE\_TIMER2 is defined. With the kind assistance of Luc Small. Thanks!\
  Updated comments in [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) concerning servers, retries, timeouts and delays. Fixed an error in [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) where recvfrom return value was not checked. Reported by Steve Childress.\
  Added Linux simulator support so simple RadioHead sketches can be compiled and run on Linux.\
  Added [RH\_TCP](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__TCP.html) driver to permit message passing between simulated sketches on Linux.\
  Added example simulator sketches.\
  Added tools/etherSimulator.pl, a simulator of the 'Luminiferous Ether' that passes messages between simulated sketches and can simulate random message loss etc.\
  Fixed a number of typos and improved some documentation.\
- 1.10 2014-05-15 \
  Added support for RFM73 modules to [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html). These 2 radios are very similar, and can interoperate with each other. Added new [RH\_NRF24::TransmitPower](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html#abf31686ee994851a27d6a9d7dc51771f) enums for the RFM73, which has a different range of available powers\
  reduced the default SPI bus speed for [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) to 1MHz, since so many modules and CPU have problems with 8MHz.\
- 1.11 2014-05-18\
  Testing [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) with RFM23BP and 3.3V Teensy 3.1 and 5V Arduinos. Updated documentation with respect to GPIO and antenna control pins for RFM23. Updated documentation with respect to transmitter power control for RFM23\
  Fixed a problem with [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) driver, where GPIO TX and RX pins were not configured during initialisation, causing poor transmit power and sensitivity on those RF22/RF23 devices where GPIO controls the antenna selection pins.
- 1.12 2014-05-20\
  Testing with RF69HW and the [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) driver. Works well with the Anarduino MiniWireless -CW and -HW boards <https://www.anarduino.com/miniwireless/> including the marvellous high powered MinWireless-HW (with 20dBm output for excellent range).\
  Clarified documentation of [RH\_RF69::setTxPower](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html#abfa6b11713f416b58f32242791dc8700) values for different models of RF69.\
  Added [RHReliableDatagram::resetRetransmissions()](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html#a01ac6fe8be733e1ccc0791d5ef44bb13).\
  Retransmission count precision increased to uin32\_t.\
  Added data about actual power measurements from RFM22 module.\
- 1.13 2014-05-23\
  setHeaderFlags(flags) changed to setHeaderFlags(set, clear), enabling any flags to be individually set and cleared by either RadioHead or application code. Requested by Steve Childress.\
  Fixed power output setting for boost power on RF69HW for 18, 19 and 20dBm.\
  Added data about actual power measurements from RFM69W and RFM69HW modules.\
- 1.14 2014-05-26\
  [RH\_RF69::init()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html#a0d78af6f999adf187861e7e3f1d52e99) now always sets the PA boost back to the default settings, else can get invalid PA power modes after uploading new sketches without a power cycle. Reported by Bryan.\
  Added new macros RH\_VERSION\_MAJOR RH\_VERSION\_MINOR, with automatic maintenance in Makefile.\
  Improvements to [RH\_TCP](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__TCP.html): constructor now honours the server argument in the form "servername:port".\
  Added YIELD to [RHReliableDatagram::recvfromAckTimeout](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html#ac72c7495936b6f655a5765faac609342). Requested by Steve Childress.\
  Fixed a problem with [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) reliable datagram acknowledgements that was introduced in version 1.13. Reported by Steve Childress.\
- 1.15 2014-05-27\
  Fixed a problem with the RadioHead .zip link.
- 1.16 2014-05-30 \
  Fixed [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) so that lastRssi() returns the signal strength in dBm. Suggested by Steve Childress.\
  Added support for getLastPreambleTime() to [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html). Requested by Steve Childress.\
  [RH\_NRF24::init()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html#afdb9eb79fec2d1f8444e5830c7267445) now checks if there is a device connected and responding, else init() will fail. Suggested by Steve Brown.\
  [RHSoftwareSPI](https://www.airspayce.com/mikem/arduino/RadioHead/classRHSoftwareSPI.html) now initialises default values for SPI pins MOSI = 12, MISO = 11 and SCK = 13.\
  Fixed some problems that prevented [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) working with mixed software and hardware SPI on different devices: a race condition due to slow SPI transfers and fast acknowledgement.\
- 1.17 2014-06-02 \
  Fixed a debug typo in [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) that was introduced in 1.16.\
  [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) now sets default power, data rate and channel in init(), in case another app has previously set different values without powerdown.\
  Caution: there are still problems with [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) and Software SPI. Do not use.\
- 1.18 2014-06-02\
  Improvements to performance of [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) statusRead, allowing [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) and Software SPI to operate on slow devices like Arduino Uno.\
- 1.19 2014-06-19\
  Added examples ask\_transmitter.pde and ask\_receiver.pde.\
  Fixed an error in the [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) doc for connection of Teensy to RF22.\
  Improved documentation of start symbol bit patterns in RH\_ASK.cpp
- 1.20 2014-06-24\
  Fixed a problem with compiling on platforms such as ATtiny where SS is not defined.\
  Added YIELD to [RHMesh::recvfromAckTimeout()](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html#a517d98d556fcc521bd17f900e939b0b3).\
- 1.21 2014-06-24\
  Fixed an issue in [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) where characters might be lost with back-to-back frames. Suggested by Steve Childress.\
  Brought previous RHutil/crc16.h code into mainline RHCRC.cpp to prevent name collisions with other similarly named code in other libraries. Suggested by Steve Childress.\
  k Fix SPI bus speed errors on 8MHz Arduinos.
- 1.22 2014-07-01\
  Update [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) documentation for common wiring connections.\
  Testing [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) with HopeRF RFM83C/RFM85 courtesy Anarduino <https://www.anarduino.com/>\
  Testing [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) with Itead Studio IBoard Pro <https://imall.iteadstudio.com/iboard-pro.html> using both hardware SPI on the ITDB02 Parallel LCD Module Interface pins and software SPI on the nRF24L01+ Module Interface pins. Documented wiring required.\
  Added support for AVR 1284 and 1284p, contributed by Peter Scargill. Added support for Semtech SX1276/77/78 and HopeRF RFM95/96/97/98 and other similar LoRa capable radios in LoRa mode only. Tested with the excellent MiniWirelessLoRa from Anarduino <https://www.anarduino.com/miniwireless>\
- 1.23 2014-07-03\
  Changed the default modulation for [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) to GFSK\_Rb250Fd250, since the previous default was not very reliable.\
  Documented [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) range tests.\
  Improvements to [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) RSSI readings so that lastRssi correctly returns the last message in dBm.\
- 1.24 2014-07-18 Added support for building RadioHead for STM32F4 Discovery boards, using the native STM Firmware libraries, in order to support Codec2WalkieTalkie (<https://www.airspayce.com/mikem/Codec2WalkieTalkie>) and other projects. See STM32ArduinoCompat.\
  Default modulation for [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) was incorrectly set to a very slow Bw125Cr48Sf4096
- 1.25 2014-07-25 The available() function will longer terminate any current transmission, and force receive mode. Now, if there is no unprocessed incoming message and an outgoing message is currently being transmitted, available() will return false.\
  [RHRouter::sendtoWait(uint8\_t\*, uint8\_t, uint8\_t, uint8\_t)](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html#a7ac935defd2418f45a4d9f391f7e0384) renamed to sendtoFromSourceWait due to conflicts with new sendtoWait() with optional flags.\
  RHMEsh and [RHRouter](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html) already supported end-to-end application layer flags, but [RHMesh::sendtoWait()](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html#a9dcb42be25d06b69a85e27189822fbc6) and RHRouter::sendToWait have now been extended to expose a way to send optional application layer flags.
- 1.26 2014-08-12 Fixed a Teensy 2.0 compile problem due yield() not available on Teensy < 3.0. \
  Adjusted the algorithm of [RH\_RF69::temperatureRead()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html#a864eae13e51279b9bca9de3fb2a062f9) to more closely reflect reality.\
  Added functions to [RHGenericDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHGenericDriver.html) to get driver packet statistics: rxBad(), rxGood(), txGood().\
  Added [RH\_RF69::printRegisters()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html#abf5be102f9291447f22b6df823455aea).\
  [RH\_RF95::printRegisters()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#af82a441a5946b538f60f31e727009750) was incorrectly printing the register index instead of the address. Reported by Phang Moh Lim.\
  [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html), added definitions for some more registers that are usable in LoRa mode.\
  [RH\_RF95::setTxPower](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#ab273e242758e3cc2ed2679ef795a7196) now uses RH\_RF95\_PA\_DAC\_ENABLE to achieve 21, 22 and 23dBm.\
  [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html), updated power output measurements.\
  Testing [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) on Teensy 3.1 with RF69 on PJRC breakout board. OK.\
  Improvements so RadioHead will build under Arduino where SPI is not supported, such as ATtiny.\
  Improvements so RadioHead will build for ATTiny using Arduino IDE and tinycore arduino-tiny-0100-0018.zip.\
  Testing [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) on ATTiny85. Reduced RAM footprint. Added helpful documentation. Caution: RAM memory is *very* tight on this platform.\
  [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) and [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html), added setIdleMode() function to allow the idle mode radio operating state to be controlled for lower idle power consumption at the expense of slower transitions to TX and RX.\
- 1.27 2014-08-13 All [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) modulation schemes now have data whitening enabled by default.\
  Tested and added a number of OOK modulation schemes to [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) Modem config table.\
  Minor improvements to a number of the faster [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) modulation schemes, but some slower ones are still not working correctly.\
- 1.28 2014-08-20 Added new [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html) driver to support Si446x, RF24/26/26, RFM24/26/27 family of transceivers. Tested with the excellent Anarduino Mini and RFM24W and RFM26W with the generous assistance of the good people at Anarduino <https://www.anarduino.com>.
- 1.29 2014-08-21 Fixed a compile error in [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html) introduced at the last minute in hte previous release.\
  Improvements to [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) modulation schemes: now include the AFCBW in teh ModemConfig.\
  ModemConfig [RH\_RF69::FSK\_Rb2Fd5](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html#a8b7db5c6e4eb542f46fec351b2084bbea23309558997f0821df4c3f26be956937) and [RH\_RF69::GFSK\_Rb2Fd5](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html#a8b7db5c6e4eb542f46fec351b2084bbeada06f635ace1b8b431e7ecc2a5415210) are now working.\
- 1.30 2014-08-25 Fixed some compile problems with ATtiny84 on Arduino 1.5.5 reported by Glen Cook.\
- 1.31 2014-08-27 Changed [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) FSK and GFSK modulations from Rb2\_4Fd2\_4 to Rb2\_4Fd4\_8 and FSK\_Rb4\_8Fd4\_8 to FSK\_Rb4\_8Fd9\_6 since the previous ones were unreliable (they had modulation indexes of 1).\
- 1.32 2014-08-28 Testing with RedBearLab Blend board <https://redbearlab.com/blend/>. OK.\
  Changed more [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) FSK and GFSK slowish modulations to have modulation index of 2 instead of 1. This required chnaging the symbolic names.\
- 1.33 2014-09-01 Added support for sleep mode in RHGeneric driver, with new mode RHModeSleep and new virtual function sleep().\
  Added support for sleep to [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html), [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html), [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html), [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html), [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) drivers.\
- 1.34 2014-09-19 Fixed compile errors in example rf22\_router\_test.\
  Fixed a problem with [RH\_NRF24::setNetworkAddress](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html#aa52be60b02d9db359c96e310abefc642), also improvements to [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) register printing. Patched by Yveaux.\
  Improvements to [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) initialisation for version 2.0 silicon.\
  Fixed problem with ambigiguous print call in RH\_RFM69 when compiling for Codec2.\
  Fixed a problem with [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) on RFM73 where the LNA gain was not set properly, reducing the sensitivity of the receiver.
- 1.35 2014-09-19 Fixed a problem with interrupt setup on [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) with Teensy3.1. Reported by AD.\
- 1.36 2014-09-22 Improvements to interrupt pin assignments for **AVR\_ATmega1284** and\_\_AVR\_ATmega1284P\_\_, provided by Peter Scargill.\
  Work around a bug in Arduino 1.0.6 where digitalPinToInterrupt is defined but NOT\_AN\_INTERRUPT is not.\
- 1.37 2014-10-19 Updated doc for connecting [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) to Arduino Mega.\
  Changes to [RHGenericDriver::setHeaderFlags()](https://www.airspayce.com/mikem/arduino/RadioHead/classRHGenericDriver.html#acb992b3c5e360e68b67e4843558bcf3b), so that the default for the clear argument is now RH\_FLAGS\_APPLICATION\_SPECIFIC, which is less surprising to users. Testing with the excellent MoteinoMEGA from LowPowerLab <https://lowpowerlab.com/shop/moteinomega> with on-board RFM69W.
- 1.38 2014-12-29 Fixed compile warning on some platforms where [RH\_RF24::send](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html#a9aaa8c5b36eccb568c87c4c9e74e7877) and [RH\_RF24::writeTxFifo](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html#afd54aecdd3cff38aca2a912c200e3fe7) did not return a value.\
  Fixed some more compiler warnings in [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html) on some platforms.\
  Refactored printRegisters for some radios. Printing to Serial is now controlled by the definition of RH\_HAVE\_SERIAL.\
  Added partial support for ARM M4 w/CMSIS with STM's Hardware Abstraction lib for Steve Childress.\
- 1.39 2014-12-30 Fix some compiler warnings under IAR.\
  RH\_HAVE\_SERIAL and Serial.print calls removed for ATTiny platforms.\
- 1.40 2015-03-09 Added notice about availability on PlatformIO, thanks to Ivan Kravets.\
  Fixed a problem with [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) where short packet lengths would occasionally not be trasmitted due to a race condition with RH\_NRF24\_TX\_DS. Reported by Mark Fox.\
- 1.41 2015-03-29 [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html), [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html), [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) and [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) improved to allow driver.init() to be called multiple times without reallocating a new interrupt, allowing the driver to be reinitialised after sleeping or powering down.
- 1.42 2015-05-17 Added support for [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) driver on Raspberry Pi, using BCM2835 library for GPIO pin IO. Contributed by Mike Poublon.\
  Tested [RH\_NRF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html) module with NRF24L01+PA+LNA SMA Antenna Wireless Transceiver modules similar to: <https://www.elecfreaks.com/wiki/index.php?title=2.4G_Wireless_nRF24L01p_with_PA_and_LNA> works with no software changes. Measured max power output 18dBm.\
- 1.43 2015-08-02 Added [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html) driver to support Nordic nRF51 family processor with 2.4GHz radio such as nRF51822, to be built on Arduino 1.6.4 and later. Tested with RedBearLabs nRF51822 board and BLE Nano kit\
- 1.44 2015-08-08 Fixed errors with compiling on some platforms without serial, such as ATTiny. Reported by Friedrich Müller.\
- 1.45 2015-08-13 Added support for using [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) on Linux and OSX (new class RHutil/HardwareSerial encapsulates serial ports on those platforms). Example examples/serial upgraded to build and run on Linux and OSX using the tools/simBuild builder. [RHMesh](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html), [RHRouter](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html) and [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) updated so they can use [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html) without polling loops on Linux and OSX for CPU efficiency.\
- 1.46 2015-08-14 Amplified some doc concerning Linux and OSX [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html). Added support for 230400 baud rate in HardwareSerial.\
  Added sample sketches nrf51\_audio\_tx and nrf51\_audio\_rx which show how to build an audio TX/RX pair with RedBear nRF51822 boards and a SparkFun MCP4725 DAC board. Uses the built-in ADC of the nRF51822 to sample audio at 5kHz and transmit packets to the receiver which plays them via the DAC.\
- 1.47 2015-09-18 Removed top level Makefile from distribution: its only used by the developer and its presence confuses some people.\
  Fixed a problem with [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) with some versions of Raspberry Pi random() that causes problems: random(min, max) sometimes exceeds its max limit.
- 1.48 2015-09-30 Added support for Arduino Zero. Tested on Arduino Zero Pro.
- 1.49 2015-10-01 Fixed problems that prevented interrupts working correctly on Arduino Zero and Due. Builds and runs with 1.6.5 (with 'Arduino SAMD Boards' for Zero version 1.6.1) from arduino.cc. Arduino version 1.7.7 from arduino.org is not currently supported.
- 1.50 2015-10-25 Verified correct building and operation with Arduino 1.7.7 from arduino.org. Caution: You must burn the bootloader from 1.7.7 to the Arduino Zero before it will work with Arduino 1.7.7 from arduino.org. Conversely, you must burn the bootloader from 1.6.5 to the Arduino Zero before it will work with Arduino 1.6.5 from arduino.cc. Sigh. Fixed a problem with [RH\_NRF905](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF905.html) that prevented the power and frequency ranges being set properly. Reported by Alan Webber.
- 1.51 2015-12-11 Changes to RH\_RF6::setTxPower() to be compatible with SX1276/77/78/79 modules that use RFO transmitter pins instead of PA\_BOOST, such as the excellent Modtronix inAir4 <https://modtronix.com/inair4.html> and inAir9 modules <https://modtronix.com/inair9.html>. With the kind assistance of David from Modtronix.
- 1.52 2015-12-17 Added [RH\_MRF89](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__MRF89.html) module to suport Microchip MRF89XA and compatible transceivers. and modules.\
- 1.53 2016-01-02 Added [RH\_CC110](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__CC110.html) module to support Texas Instruments CC110L and compatible transceivers and modules.\
- 1.54 2016-01-29 Added support for ESP8266 processor on Arduino IDE. Examples serial\_reliable\_datagram\_\* are shown to work. CAUTION: SPI not supported yet. Timers used by [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) are not tested. The GHz radio included in the ESP8266 is not yet supported.
- 1.55 2016-02-12 Added macros for htons() and friends to [RadioHead.h](https://www.airspayce.com/mikem/arduino/RadioHead/RadioHead_8h_source.html). Added example sketch serial\_gateway.pde. Acts as a transparent gateway between [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) and [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html), and with minor mods acts as a universal gateway between any 2 RadioHead driver networks. Initial work on supporting STM32 F2 on Particle Photon: new platform type defined. Fixed many warnings exposed by test building for Photon. Particle Photon tested support for [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html), [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html), SPI, [RH\_CC110](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__CC110.html) etc. Added notes on how to build RadioHead sketches for Photon.
- 1.56 2016-02-18 Implemented timers for [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) on ESP8266, added some doc on IO pin selection.
- 1.57 2016-02-23 Fixed an issue reported by S3B, where [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) would sometimes not clear the rxbufvalid flag.
- 1.58 2-16-04-04 Tested [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) with Arduino Due. OK. Updated doc.\
  Added support for all ChipKIT Core supported boards <https://chipkit.net/wiki/index.php?title=ChipKIT_core> Tested on ChipKIT Uno32.\
  Digilent Uno32 under the old MPIDE is no longer formally supported but may continue to work for some time.\
- 1.59 2016-04-12 Testing with the excellent Rocket Scream Mini Ultra Pro with the RFM95W and RFM69HCW modules from <https://www.rocketscream.com/blog/product/mini-ultra-pro-with-radio/> (915MHz versions). Updated documentation with hints to suit. Caution: requires Arduino 1.6.8 and Arduino SAMD Boards 1.6.5. See also <https://www.rocketscream.com/blog/2016/03/10/radio-range-test-with-rfm69hcw/> for the vendors tests and range with the RFM69HCW version. They also have an RF95 version equipped with TCXO temperature controllled oscillator for extra frequency stability and support of very slow and long range protocols. These boards are highly recommended. They also include battery charging support.
- 1.60 2016-06-25 Tested with the excellent talk2 Whisper Node boards (<https://talk2.wisen.com.au/> and <https://bitbucket.org/talk2/>), an Arduino Nano compatible board, which include an on-board RF69 radio, external antenna, run on 2xAA batteries and support low power operations. RF69 examples work without modification. Added support for ESP8266 SPI, provided by David Skinner.
- 1.61 2016-07-07 Patch to RH\_ASK.cpp for ESP8266, to prevent crashes in interrupt handlers. Patch from Alexander Mamchits.
- 1.62 2016-08-17 Fixed a problem in [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) where \_rxInverted was not properly initialised. Reported by "gno.sun.sop". Added support for waitCAD() and isChannelActive() and setCADTimeout() to RHGeneric. Implementation of [RH\_RF95::isChannelActive()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a6f4fef2a1f40e704055bff09799f08cf) allows the RF95 module to support Channel Activity Detection (CAD). Based on code contributed by Bent Guldbjerg Christensen. Implmentations of isChannelActive() plus documentation for other radio modules wil be welcomed.
- 1.63 2016-10-20 Testing with Adafruit Feather 32u4 with RFM69HCW. Updated documentation to reflect.\
- 1.64 2016-12-10 [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) now initialises \_seenids. Fix from Ben Lim.\
  In [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html), added get\_temperature().\
  In [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html), added support for AES packet encryption, which required a slight change to the on-air message format.\
- 1.65 2017-01-11 Fixed a race condition with [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html) that prevented ACKs being reliably received.\
  Removed code in [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html) that enabled the DC-DC converter. This seems not to be a necessary condition for the radio to work and is now left to the application if that is required.\
  Proven interoperation between nRF51822 and nRF52832.\
  Modification and testing of [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html) so it works with nRF52 family processors, such Sparkfun nRF52832 breakout board, with Arduino 1.6.13 and Sparkfun nRF52 boards manager 0.2.3 using the procedures outlined in <https://learn.sparkfun.com/tutorials/nrf52832-breakout-board-hookup-guide>\
  Caution, the Sparkfun development system for Arduino is still immature. We had to rebuild the nrfutil program since the supplied one was not suitable for the Linux host we were developing on. See <https://forum.sparkfun.com/viewtopic.php?f=32&t=45071> Also, after downloading a sketch in the nRF52832, the program does not start executing cleanly: you have to reset the processor again by pressing the reset button. This appears to be a problem with nrfutil, rather than a bug in RadioHead.
- 1.66 2017-01-15 Fixed some errors in (unused) register definitions in [RH\_RF95.h](https://www.airspayce.com/mikem/arduino/RadioHead/RH__RF95_8h_source.html).\
  Fixed a problem that caused compilation errors in [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html) if the appropriate board support was not installed.
- 1.67 2017-01-24 Added [RH\_RF95::frequencyError()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a96154a00662d73f69b9858597c8d4c9b) to return the estimated centre frequency offset in Hz of the last received message
- 1.68 2017-01-25 Fixed arithmetic error in [RH\_RF95::frequencyError()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a96154a00662d73f69b9858597c8d4c9b) for some platforms.
- 1.69 2017-02-02 Added [RH\_RF95::lastSNR()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a13efb0779e4bc522986f272201cb43cf) and improved lastRssi() calculations per the manual.
- 1.70 2017-02-03 Added link to Binpress commercial license purchasing.
- 1.71 2017-02-07 Improved support for STM32. Patch from Bent Guldbjerg Christensen.
- 1.72 2017-03-02 In [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html), fixed a problem where some important properties were not set by the ModemConfig. Added properties 2007, 2008, 2009. Also properties 200a was not being set in the chip. Reported by Shannon Bailey and Alan Adamson. Fixed corresponding convert.pl and added it to the distribution.
- 1.73 2017-03-04 Significant changes to [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html) and its API. It is no longer possible to change the modulation scheme programatically: it proved impossible to cater for all the possible crystal frequencies, base frequency and modulation schemes. Instead you can use one of a small set of supplied radio configuration header files, or generate your own with Silicon Labs WDS application. Changing modulation scheme required editing RH\_RF24.cpp to specify the appropriate header and recompiling. convert.pl is now redundant and removed from the distribution.
- 1.74 2017-03-08 Changed [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) so it would not ACK messages heard addressed to other nodes in promiscuous mode.\
  Added [RH\_RF24::deviceType()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html#aa368cbdfd7709d4ea372c6c5bf414751) to return the integer value of the connected device.\
  Added documentation about how to connect RFM69 to an ESP8266. Tested OK.\
  [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html) was not correctly changing state in sleep() and setModeIdle().\
  Added example rf24\_lowpower\_client.pde showing how to put an arduino and radio into a low power mode between transmissions to save battery power.\
  Improvements to [RH\_RF69::setTxPower](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html#abfa6b11713f416b58f32242791dc8700) so it now takes an optional ishighpowermodule flag to indicate if the connected module is a high power RFM69HW, and so set the power level correctly. Based on code contributed by bob.
- 1.75 2017-06-22 Fixed broken compiler issues with [RH\_RF95::frequencyError()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a96154a00662d73f69b9858597c8d4c9b) reported by Steve Rogerson.\
  Testing with the very excellent Rocket Scream boards equipped with RF95 TCXO modules. The temperature controlled oscillator stabilises the chip enough to be able to use even the slowest protocol Bw125Cr48Sf4096. Caution, the TCXO model radios are not low power when in sleep (consuming about ~600 uA, reported by Phang Moh Lim).\
  Added support for EBYTE E32-TTL-1W and family serial radio transceivers. These RF95 LoRa based radios can deliver reliable messages at up to 7km measured.
- 1.76 2017-06-23 Fixed a problem with [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) hanging on transmit under some mysterious circumstances. Reported by several people at <https://forum.pjrc.com/threads/41878-Probable-race-condition-in-Radiohead-library?p=146601#post146601> \
  Increased the size of rssi variables to 16 bits to permit RSSI less than -128 as reported by RF95.
- 1.77 2017-06-25 Fixed a compilation error with lastRssi().\
- 1.78 2017-07-19 Fixed a number of unused variable warnings from g++.\
  Added new module [RHEncryptedDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHEncryptedDriver.html) and examples, contributed by Philippe Rochat, which adds encryption and decryption to any RadioHead transport driver, using any encryption cipher supported by ArduinoLibs Cryptographic Library <https://rweather.github.io/arduinolibs/crypto.html> Includes several examples.\
- 1.79 2017-07-25 Added documentation about 'Passing Sensor Data Between RadioHead nodes'.\
  Changes to [RH\_CC110](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__CC110.html) driver to calculate RSSI in dBm, based on a patch from Jurie Pieterse.\
  Added missing passthroughmethoids to [RHEncryptedDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHEncryptedDriver.html), allowing it to be used with [RHDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHDatagram.html), [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html) etc. Tested with [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html). Added examples
- 1.80 2017-10-04 Testing with the very fine Talk2 Whisper Node LoRa boards <https://wisen.com.au/store/products/whisper-node-lora> an Arduino compatible board, which include an on-board RFM95/96 LoRa Radio (Semtech SX1276), external antenna, run on 2xAAA batteries and support low power operations. RF95 examples work without modification. Use Arduino Board Manager to install the Talk2 code support. Upload the code with an FTDI adapter set to 5V.\
  Added support for SPI transactions in development environments that support it with SPI\_HAS\_TRANSACTION. Tested on ESP32 with RFM-22 and Teensy 3.1 with RF69 Added support for ESP32, tested with RFM-22 connected by SPI.\
- 1.81 2017-11-15 [RH\_CC110](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__CC110.html), moved setPaTable() from protected to public.\
  [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) modem config Bw125Cr48Sf4096 altered to enable slow daat rate in register 26 as suggested by Dieter Kneffel. Added support for nRF52 compatible Arm chips such as as Adafruit BLE Feather board <https://www.adafruit.com/product/3406>, with a patch from Mike Bell.\
  Fixed a problem where rev 1.80 broke Adafruit M0 LoRa support by declaring bitOrder variable always as a unsigned char. Reported by Guilherme Jardim.\
  In [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html), all modes now have AGC enabled, as suggested by Dieter Kneffel.\
- 1.82 2018-01-07 Added guard code to [RH\_NRF24::waitPacketSent()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html#a62904aa954e2bbf0a5c37bddb768b5a5) so that if the transmit never completes for some reason, the code will eventually return with FALSE. Added the low-datarate-optimization bit to config for [RH\_RF95::Bw125Cr48Sf4096](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#ab9605810c11c025758ea91b2813666e3a241b28dcbb17f8a86e3f8edd03c51b21). Fix from Jurie Pieterse to ensure [RH\_CC110::sleep](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__CC110.html#aab9e12b3206e733d8e200547211781ea) always enters sleep mode. Update ESP32 support to include ASK timers. [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) module is now working on ESP32.
- 1.83 2018-02-12 Testing adafruit M0 Feather with E32. Updated [RH\_E32](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__E32.html) documentation to show suggested connections and contructor initialisation.\
  Fixed a problem with [RHEncryptedDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHEncryptedDriver.html) that could cause a crash on some platforms when used with [RHReliableDatagram](https://www.airspayce.com/mikem/arduino/RadioHead/classRHReliableDatagram.html). Reported by Joachim Baumann.\
  Improvments to doxygen doc layout in [RadioHead.h](https://www.airspayce.com/mikem/arduino/RadioHead/RadioHead_8h_source.html)
- 1.84 2018-05-07 Compiles with Roger Clarkes Arduino\_STM32 <https://github.com/rogerclarkmelbourne/Arduino_STM32>, to support STM32F103C etc, and STM32 F4 Discovery etc.\
  Tested STM32 F4 Discovery board with [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html), [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) and [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html).
- 1.85 2018-07-09 [RHGenericDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHGenericDriver.html) methods changed to virtual, to allow overriding by RHEncrypredDriver: lastRssi(), mode(), setMode(). Reported by Eyal Gal.\
  Fixed a problem with compiling [RH\_E32](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__E32.html) on some older IDEs, contributed by Philippe Rochat.\
  Improvements to [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) to improve detection of bad packets, contributed by PiNi.\
  Fixed an error in [RHEncryptedDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHEncryptedDriver.html) that caused incorrect message lengths for messages multiples of 16 bytes when STRICT\_CONTENT\_LEN is defined.\
  Fixed a bug in [RHMesh](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html) which causes the creation of a route to the address which is the byte behind the end of the route array. Reported by Pascal Gillès de Pélichy.\
- 1.86 2018-08-28 Update commercial licensing, remove binpress.
- 1.87 2018-10-06 [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) now resets all registers to default state before initialisation commences. Suggested by Wothke.\
  Added RH\_ENABLE\_EXPLICIT\_RETRY\_DEDUP which improves the handling of duplicate detection especially in the case where a transmitter periodically wakes up and start transmitting from the first sequence number. Patch courtesy Justin Newitter. Thanks.
- 1.88 2018-11-13 Updated to support ATTiny using instructions in <https://medium.com/jungletronics/attiny85-easy-flashing-through-arduino-b5f896c48189> Updated examples ask\_transmitter and ask\_receiver to compile cleanly on ATTiny. Tested using ATTiny85 and Arduino 1.8.1. \
- 1.89 2018-11-15 Testing with ATTiny core from <https://github.com/SpenceKonde/ATTinyCore> and [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html), using example ask\_transmitter. This resulted in 'Low Memory, instability may occur', and the resulting sketch would transmit only one packet. Suggest ATTiny users do not use this core, but use the one from <https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json> as described in <https://medium.com/jungletronics/attiny85-easy-flashing-through-arduino-b5f896c48189> \
  Added support for [RH\_RF95::setSpreadingFactor()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#abea770963212a64b35169f0f0c35c14d), [RH\_RF95::setSignalBandwidth()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a02ba623bba31f200e50e46686ec61176), [RH\_RF95::setLowDatarate()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a8e2df6a6d2cb192b13bd572a7005da67) and [RH\_RF95::setPayloadCRC()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a9b402c77236b0dfe3ec68e953faa02dd). Patch from Brian Norman. Thanks.\
- 1.90 2019-05-21 Fixed a block size error in RhEncryptedDriver for the case when using STRICT\_CONTENT\_LEN and sending messages of exactly \_blockcipher.blockSize() bytes in length. Reported and patched by Philippe Rochat. Patch from Samuel Archibald to prevent compile errors with RH\_AAK.cpp fo ATSAMD51. Fixed a probem in [RH\_RF69::setSyncWords](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html#aeadfa5f2783c821de73ecb09c50000d4) that prevented setSyncWords(NULL, 0) correctly disabling sync detection and generation. Reported by Federico Maggi. RHHardwareSPI::usingInterrupt() was a noop. Fixed to call SPI.usingInterrupt(interrupt);.
- 1.91 2019-06-01 Fixed a problem with new RHHardwareSPI::usingInterrupt() that prevented compilation on ESP8266 which does not have that call.
- 1.92 2019-07-14 Retested serial\_reliable\_datagram\_client.pde and serial\_reliable\_datagram\_server.pde built on Linux as described in their headers, and with USB-RS485 adapters. No changes, working correctly. Testing of nRF5232 with Sparkfun nRF52 board support 0.2.3 shows that there appears to be a problem with interrupt handlers on this board, and none of the interrupt based radio drivers can be expected to work with this chip. Ensured all interrupt routines are flagged with ICACHE\_RAM\_ATTR when compiled for ESP8266, to prevent crashes.
- 1.94 2019-09-02 Fixed a bug in [RHSoftwareSPI](https://www.airspayce.com/mikem/arduino/RadioHead/classRHSoftwareSPI.html) where [RHGenericSPI::setBitOrder()](https://www.airspayce.com/mikem/arduino/RadioHead/classRHGenericSPI.html#a76fa1e24aa0f686e66fa71f95ee7c0b4) has no effect for on [RHSoftwareSPI](https://www.airspayce.com/mikem/arduino/RadioHead/classRHSoftwareSPI.html). Reported by Peter.\
  Added support in [RHRouter](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html) for a node to optionally be leaf node, and not participate as a router in the network. See RHRouter::setNodeTypePatch from Alex Evans.\
  Fixed a problem with ESP32 causing compile errors over missing SPI.usingInterrupt().\
- 1.95 2019-10-14 Fixed some typos in RH\_RF05.h macro definitions reported by Clayton Smith.\
  Patch from Michael Cain from [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) on ESP32, untested by me.\
  Added support for RPi Zero and Zero W for the RF95, contributed by Brody Mahoney. Not tested by me.\
- 1.96 2019-10-14 Added examples for RPi Zero and Zero W to examples/raspi/rf95, contributed by Brody Mahoney not tested by me. \
- 1.97 2019-11-02 Added support for Mongoose OS, contributed by Paul Austen.
- 1.98 2020-01-06 Rationalised use of RH\_PLATFORM\_ATTINY to be consistent with other platforms.\
  Added support for RH\_PLATFORM\_ATTINY\_MEGA, for use with Spencer Konde's megaTinyCore <https://github.com/SpenceKonde/megaTinyCore> on Atmel megaAVR ATtiny 1-series chips. Tested with AtTiny 3217, 3216 and 1614, using [RH\_Serial](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__Serial.html), [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html), and [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) drivers.\
- 1.99 2020-03-07 Release under GPL V3
- 1.100 2020-03-12 Fixed a problem that prevented compilation of [RH\_NRF51](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF51.html) on Arduino for Sparkfun nRF52832 Breakout board.\
- 1.101 2020-04-10 Tested nRF52832 with RFM69W module and [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html), using Software SPI and hardware interrutps OK.\
  Fixed warnings about 'deleting object of polymorphic class' if driver is dynamically allocated.\
  Fixed problems in [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) and HardwareSPI to work with STM32F4 Discovery with latest version of stm32duino <https://github.com/stm32duino/Arduino_Core_STM32>. Testing with stm32duino 1.8.0 downloaded with Board Manager per <https://github.com/stm32duino/Arduino_Core_STM32> . Now builds and run [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) examples with STM32F4 Discovery board. Build without error for STM32 F1 and F4 but Does not compile for Generic STM32F3.
- 1.102 2020-05-15 Updated [RH\_RF95::setPayloadCRC](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#a9b402c77236b0dfe3ec68e953faa02dd) to affect CRC generation on outgoing packets as well as CRC detection and checking on incoming packets. Added new modem config for [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html). [RH\_RF95::Bw125Cr45Sf2048](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#ab9605810c11c025758ea91b2813666e3a56e71534d8b36bf7db69dbc85eb96666) Bw = 125 kHz, Cr = 4/5, Sf = 2048chips/symbol, CRC on. Slow+long range. Tested against RPI with LoRa-file-ops driver <https://github.com/starnight/LoRa/tree/file-ops> and send.c test program. Fixed a problem with (re-)definition of SS on ESP32, reported and fixed by Justin Newitter.
- 1.103 2020-05-30 Fixed some errors in [RH\_RF95::setTxPower](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html#ab273e242758e3cc2ed2679ef795a7196) which cased the power levels to be set incorrectly. Checked operation and improved documentation. Valid settings are: 2 to 20 (useRFO false) and 0 to 15 (useRFO true). 18, 19 and 20 (useRFO false) turn on the PA\_DAC. Fixed RF95 examples to reflect correct use. Added [RH\_ABZ](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ABZ.html) driver, which supports the muRata CMWX1ZZABZ (TypeABZ) module which includes an STM32L0 processor, a SX1276 LoRa radio and an antenna switch. Requires the Grumpy Old Pizza Arduino Core installed per <https://github.com/GrumpyOldPizza/ArduinoCore-stm32l0> Examples provided.
- 1.104 2020-06-08 Fixed a problem with new [RH\_ABZ](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ABZ.html) module that prevents compilation with standard 0.0.10 version of STM32L0 \
  Arduino Core installed with Board Manager: STM32L0\_EXTI\_CONTROL\_PRIORITY\_CRITICAL is only available in later versions.\
- 1.105 2020-06-03 Added support for [RH\_ABZ](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ABZ.html) on STM32L072xx on Grumpy Old Pizza Arduino Core\
- 1.106 2020-06-16 Patch from Livio Tenze for [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) to fix a problem with interrupts on on ESP8266.\
  Added examples/rf22/rf22\_cw, with example showing how to emit a carrier wave (CW).\
  Reverted delay in [RHSPIDriver::init()](https://www.airspayce.com/mikem/arduino/RadioHead/classRHSPIDriver.html#a7ba5e6fc53e02ff8125218bc296b4557) back to 100ms for all platforms except ABZ, where 100ms interferes with the USB serial port with at least some versions of the core.\
  Updated and clarified documentation about TCXO use in [RH\_ABZ](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ABZ.html) and examples.\
  Fixed documentation SS->NSEL pin for [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) with AtMega. Seems that SS on that platform is now defined as pin 10, not 53. Dont know when that changed.\
- 1.107 2020-06-26 Improvements to [RHEncryptedDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHEncryptedDriver.html), so that you will get an explanatory error message if you include [RHEncryptedDriver.h](https://www.airspayce.com/mikem/arduino/RadioHead/RHEncryptedDriver_8h_source.html) without enabling the class with RH\_ENABLE\_ENCRYPTION\_MODULE in [RadioHead.h](https://www.airspayce.com/mikem/arduino/RadioHead/RadioHead_8h_source.html).\
  Fixed newly introduced errors when compiling for ATTiny 25/45/85.\
- 1.108 2020-07-05 Fixed a problem with [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html) on ESP8266 introcuced in version 1.106 which prevented messages being received. Some other cleanups in [RH\_RF22](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF22.html)\
- 1.109 2020-07-23 Fixed a problem that prevented [RHEncryptedDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHEncryptedDriver.html) compiling when RH\_ENCRYPTED\_DRIVER was enabled.\
  Added optiona hops argument to [RHRouter](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html) and [RHMesh](https://www.airspayce.com/mikem/arduino/RadioHead/classRHMesh.html) recvfromAck() and receivedFomAckTimeout() to allow the hop count to be retreived if desired.
- 1.110 2020-07-28 Fixed a problem where \_spi.beginTransaction and \_spi.endTransaction were missing from [RHSPIDriver::spiRead](https://www.airspayce.com/mikem/arduino/RadioHead/classRHSPIDriver.html#ad25b493321b5aa9863eabe696f97d6d9).
- 1.111 2020-07-30 Fixed some compilation problems on some platforms with RH\_PLATFORM\_ATTINY\_MEGA and Kondes MegaTinyCore 1.1.2.\
  Fixed some other errors with Kondes MegaTinyCore 2.0.5: F\_CPU\_CORRECTED no longer exists, bitOrder and PinStatus no longer needed.\
  Improved detection of RH\_PLATFORM\_ATTINY\_MEGA by looking for defined(MEGATINYCORE), defined in later versions of MegaTinyCore.
- 1.112 2020-08-05 Fixed some compiler warnings in STM32 Discovery and other processors.\
  Added support for ST's Arduino Core STM32, <https://github.com/stm32duino/Arduino_Core_STM32> to [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html), per <https://github.com/r-map/rmap/commit/edf9931b21cb7df5b4f67835307255e0fcb301bb>.\
  Added documentation about requirements for code contributions.\
  Added library.properties file that some IDEs need.\
  Added support for multithreaded [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) support on Raspberry Pi, courtesy Tilman Glötzner.\
  Includes example programs, including for the Dragino Lora/GPS Hat which send GPS coordinates.\
- 1.113 2020-10-15 Changes to [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) on SpenceKonde's megaTinyCore so it will use TCB0 on platforms where TCB1 is not available.\
  Minor imprvements to documentation.\
  Move to local git for source code control.\
  Added support for [RH\_ABZ::deinit()](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ABZ.html#a40d9188585e5bd75bd44929b30d408cd) for Matt Way. Fixed compilation error in [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) caused by changes to interrupt API in Arduino\_Core\_STM32 1.9
- 1.114 2021-03-24 Fixed compile warnings, errors on some platforms, in RH\_ASK.cpp for STM32 core 1.9.0 to do with odd behaviour of callback\_function\_t.\
  Fixed some problems with SPI transactions in [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html) and [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html) that affected operations with STM32F030F4. Reported and patched by Adam De Muri.\
  Added tools/createGPX.pl, contributed by Tilman Glötzner: A perl script to process the dump files that can be produced with the Dragino LoRa-GPS-hat and rf95\_client2 + rf95\_server2. The programs exchange sequence numbers, timestamps and gps coordinates via Lora which can be used for range measurements or visualization. The perl script is meant for post processing and converts the log files into Gpx-files which in turn can be imported to google maps.\
  Added support for MRF89XAM8A, which has support for different frequency bands to [RH\_MRF89](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__MRF89.html). Patch courtesy Michael Kefeder.
- 1.115 2021-03-24 Fix compile error in new MRF89XAM8A support.
- 1.116 2021-03-30 Patch from Vlasta Hajek: 1. Made [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) usable again for ATTINY after breaking changes.
  1. Added the possibility to use Timer 1 on ATtiny8x. Tested on ATtiny 85 and ATtiny84 for more than a year.
  2. Added patch for ESP32 from jPerotto. This finally makes receiving via [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) on ESP32 without panics. Tested for more than 6 months.\
- 1.117 2021-05-26 Added documention to [RH\_MRF89](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__MRF89.html) about how to achieve 1μA power consumption in sleep mode. Courtesy Fernando Faria.\
  Improved documentation for the meaning of 'len' in all recv\*, as suggested by Sean. E. Sean.\
  waitAvailable and waitAvaiableTimeout now take an optional polldelay argument that can be useful for introducing on multitasking systems where a driver requires polling.\
  Fixed compile errors with forward declarations in [RH\_E32.h](https://www.airspayce.com/mikem/arduino/RadioHead/RH__E32_8h_source.html) and [RH\_Serial.h](https://www.airspayce.com/mikem/arduino/RadioHead/RH__Serial_8h_source.html) on Ardiono IDE on Windows reported by Skywodd.
- 1.118 2021-07-16 Added a 1 us delay in [RHSPIDriver::spiWrite](https://www.airspayce.com/mikem/arduino/RadioHead/classRHSPIDriver.html#a3b1e1233ef51cfd48b3f050ca080003a) as recommended in <https://forum.pjrc.com/attachment.php?attachmentid=10948&d=1499109224> for corect operation with some fast processors. \
  Tested Ebyte E22-900T22S radios with serial interface and the examples from examples/serial/serial\_reliable\_datagram\_\* on Linux. These radios implement a transparent serial connection using LORA. They can also be configured as independent relays. You can alter the default configuration of the radios (including frequency, transmission rates, node addresses etc) by using the Ebyte RF Settings for E22 tool from <https://www.cdebyte.net/download-tools> and after setting the device to configuraiotn mode (M1 high: temporarily remove the M1 link). Caution, to use this tool on Windows, you also must install the CH340 USB-Serial port driver, see <https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all#windows-710> \
  These modules can also be configured programatically, but this is not supported by RadioHead. \
  Fixed compile errors to do with RH\_DRAM\_ATTR on non-ESP-32 platforms. \
  Fixed problems reported with crashes in [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) on STM32 boards with core >= 1.9.0 due to incorrect declaration of interrupt function. \
- 1.119 2021-08-02 Changes to [RadioHead.h](https://www.airspayce.com/mikem/arduino/RadioHead/RadioHead_8h_source.html) RHHardwareSPI.cpp and RHSPIDriver.cpp for ESP32 support provided by Juliano Perotto.
- 1.120 2021-11-13 Added intial support for Raspberry Pi Pico, using the Raspberry Pi Pico/RP2040 core by Earle F. Philhower, version 1.93, installed per <https://arduino-pico.readthedocs.io/_/downloads/en/latest/pdf/> [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) works with default pins (11 and 12). But it seems that interrupt callbacks (needed by most SPI based radio drivers in RadioHead) are not working (yet) in this core, at least when compiled on our Linux platform. It appears there is some bug in std::map that causes the interrupt handling to not work correctly (which I have been able to reproduce in a simple sketch that only uses std::map). This is very strange. Interrupts *are* supported and work in the alternative Arduino MBED OS RP2040 core version 2.4.1, but there are other mysterious crashes RadioHead when a radio driver reads SPI inside an interrupt. But [RH\_ASK](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html) also works with this core. So the result (so far) is partial support of RadioHead using either core (so far). We will revisit this when either core is updated\
  On ESP32, added support for using the non-default HSPI bus by defining RH\_ESP32\_USE\_HSPI.\
  Improved the reading of RSSI for the last packet in [RH\_CC110](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__CC110.html): seems that it was being read too soon. Now read it from the end received packet with RH\_CC110\_APPEND\_STATUS.\
  Added [RH\_LoRaFileOps](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__LoRaFileOps.html), driver on RPi+Linux and using LoRa-file-ops Linux driver ioctls to transmit and receive RadioHead compatible messages via SX1276/77/78/79 and compatible radios. Requires a modified version of LoRa-file-ops driver to be installed, and a compatible radio to be connected appropriately: <https://github.com/starnight/LoRa/tree/file-ops> \
- 1.121 2022-02-02 Restored [RH\_RF95](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF95.html) code to clear the IRQ flags (twice).\
- 1.122 2023-05-20 Added [RHRouter::getNextValidRoutingTableEntry()](https://www.airspayce.com/mikem/arduino/RadioHead/classRHRouter.html#ae1495879c83e3ce803ec9c36009ae592) contributed by w...\
  Various compatibility imnprovements for STM32L0 etc from Calin Radoni.\
  Added ability to overriding the value of RH\_ENABLE\_EXPLICIT\_RETRY\_DEDUP via a compiler arg. Example from PlatformIO: build\_flags = -D"RH\_ENABLE\_EXPLICIT\_RETRY\_DEDUP=1" Contributed by Justin Newitter.\
  Fixed an error in the header lengths in [RH\_TCP](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__TCP.html), which could result in the last octet of the payload being lost. checkForEvents() now returns false instead of exit() in case of IO failure\
- 1.123 2023-08-07 Added support for Arduino Uno R4 Minima.
- 1.124 2023-08-09 Extended support for Arduino Uno R4 to Arduino Uno R4 WIFI
- 1.125 2023-08-14 Improved support for Arduino Uno R4: ATOMIC\_BLOCK\_START and ATOMIC\_BLOCK\_END are no longer defined since they hang on R4, and are not necessary since they have SPI\_HAS\_TRANSACTION
- 1.126 2023-11-24 ESP8266 support now uses IRAM\_ATTR instead of ICACHE\_RAM\_ATTR. This should work fine with core 2.7.4 and later.\
  Changes to definitions of ATOMIC\_BLOCK\_START and ATOMIC\_BLOCK\_END for RH\_PLATFORM\_ESP32: Previous use of XTOS\_DISABLE\_ALL\_INTERRUPTS not suported for ESP32C3. Now uses ATOMIC\_ENTER\_CRITICAL() and ATOMIC\_EXIT\_CRITICAL() which appear to be supported for all platforms in Arduino esp32 package.\
- 1.127 2024-01-07 Added support for SX126x family radios, and also for the STM32WLE5xx and STM32WLE4xx families of ARM procedssors that have a SX126x radio built in, and as used in the LoRa-E5-HF module (which is used in WiO-E5 mini development board), the LoRa-E5-LF module and the NUCLEO\_WL55JC1 development board. Tested with WiO-E5 mini development board, but no standalone SPI versions of this radio.
- 1.128 2024-01-12 Added missing sx126x examples to distribution.
- 1.129 2024-03-21 Rename all .pde sketches to .ino Significant changes to [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) to support other modules such as the NiceRF LoRa1262 family. <https://www.nicerf.com/lora-module/915mhz-lora-module-lora1262.html> Sample client and server sketches demonstrating use, compatible with Teensy and other 3.3V compatible Arduinos.
- 1.130 2024-04-12 Adjustments to [RHHardwareSPI](https://www.airspayce.com/mikem/arduino/RadioHead/classRHHardwareSPI.html) fopr compatibility with RAKwireless RAK4360/RAK4361, contributed by gfja. Fixed a preprocessor typo in unused code in RHHardwareSPI.cpp, reported by brodymahoney.
- 1.131 2024-07-02 Fixed problem with failed compilation in RH\_ASK.cpp, when used with ESP 32 board library version 3.o or greated because the Espressif library timer API changed.\
- 1.132 2024-07-08 Fixed problem with SX126x where a packet recieved with a CRC error would leave the chip in standby mode but [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) thought it was still in RX mode. Reported by kalev.\
- 1.133 2024-07-08 Revisit SX126x RX CRC error handling with the assistance of kalev.
- 1.134 2024-07-10 Improvements to SX126x contributed by kalev:\
  1. Save IRQ flags for debugging outside interrupt handler. every time the handler is invoked save IRQ flags and rise \_iflag.\
  2. runtime set on/off IRQ mask. This gives possibility to investigate erroneous packets. \
  3. introduce raw mode send and receive for debugging.\
  4. add getFrequencyError() If receiver and sender main clock frequencies are off ( usually when pairing sx126x and sx127x ) it's difficult to adjust other party's ( usually sx127x ) frequency.\
- 1.135 2024-07-12 Fixed a problem in [RHSPIDriver](https://www.airspayce.com/mikem/arduino/RadioHead/classRHSPIDriver.html): if the Slave Select pin was set to 0xff, then it would still drive the SS pin. This broke use of EEPROM on STM32wl. Reported and fixed by Craig Zych.
- 1.136 2024-07-25 Fixed a typo in the comments for the MOSI pin number for the alternative ESP32 HSPI interface.\
  Examples were not included in idstribution since names changed to .ino
- 1.137 2025-01-03 Fixed a problem where Timer definitions for RP2350 are differnet to RP2340 Reported and patched by Conor O'Neill.
- 1.138 2025-01-05 Added support for Heltec CubeCell modules, including the builtin SX126x radio. Updated sx1262\_client.ino and sx1262\_server.ino to demonstrate usage.
- 1.139 2025-01-07 Updated CubeCell support for Heltec CubeCell board 1.5.0 installed in Arduino IDE per <https://docs.heltec.org/en/node/asr650x/asr650x_general_docs/quick_start/cubecell-use-arduino-board-manager.html>
- 1.140 2025-01-07 Fixed a compile problem on some platforms like PlatformIO to do with nullptr.
- 1.141 2025-01-08 Fixed another nullptr compile problem on Arduino 2.3.4
- 1.142 2025-01-11 Improvements to [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) to support sleep mode better, This requires us to waituntilNotBusy() *after* NSS has been asserted, not before.
- 1.143 2025-01-21 Extended Cube Cell Board support to all Cube Cell board variants currently supported by Cube Cell 1.5.0.
- 1.144 2026-01-02 Removed some leftover test code from [RH\_RF69](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF69.html). Fixed typos in [RH\_RF24.h](https://www.airspayce.com/mikem/arduino/RadioHead/RH__RF24_8h_source.html) Added RSSItodBm() to [RH\_RF24](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__RF24.html) Tested [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) driver with LLCC68 (almost identical to SX1262) in Ra-01SC module. This required a incompatible update to [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html): The Ra-01SC does not have a TCXO, but [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) always configured a TCXO: which prevents it working with radio modules without a TCXO. The call in init() to setTCXO(3.3, 100) has been removed. Now if you have a TCXO, you *must* make the call to setTCXO() yourself after init() returns. Some changes to [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) to ensure waitUntilNotBusy() is not called inside an ATOMIC\_BLOCK as it is thought this might interfere with timekeeping on some systems with FreeRTOS. Updated documentation and examples to suit LLCC68
- 1.145 2026-01-05 Fixed a bug in [RH\_SX126x](https://www.airspayce.com/mikem/arduino/RadioHead/classRH__SX126x.html) driver where receipt of an invalid message would prevent further messages being received.\
- 1.146 2026-09-15 Fixed misleading routing tables in rf22\_router\_\* examples Added patch for extension supporting the SX126x with a raspberry. Developed and tested it on a raspberrypi3. Contributed by tilman.
- 1.147 2026-10-22 Fixed a buffer overflow in the interrupt array when init() is called too often in drivers RH\_RF69.cpp, RH\_RF22.cpp, RH\_RF24.cpp, RH\_RF95.cpp, RH\_SX126x.cpp, RH\_CC110.cpp, and RH\_MRF89.cpp. Reported and patched by Adam De Muri.

**Author**

- Mike McCauley. DO NOT CONTACT THE AUTHOR DIRECTLY. USE THE GOOGLE GROUP GIVEN ABOVE

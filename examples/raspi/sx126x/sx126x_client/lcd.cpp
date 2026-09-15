// lcd.cpp
// -*- mode: C++ -*-
//
// Functions to support a LCD screen connected to I2C bus
// Requires Pigpio GPIO library.
//(9/7/2026)   Contributed by Tilman Glötzner. 


#include <pigpio.h>
#include <lcd.h>

int lcdHandle = -1; // pigpio I2C handle

// Pulse the enable pin to latch data into the LCD controller
void lcdToggleEnable(int bits) {
    gpioDelay(500); // 500 microseconds
    i2cWriteByte(lcdHandle, (bits | ENABLE));
    gpioDelay(500);
    i2cWriteByte(lcdHandle, (bits & ~ENABLE));
    gpioDelay(500);
}

// Split 8-bit characters/commands into two 4-bit nibbles over I2C
void lcdByte(int bits, int mode) {
    int bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT;
    int bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT;

    // Send high nibble
    i2cWriteByte(lcdHandle, bits_high);
    lcdToggleEnable(bits_high);

    // Send low nibble
    i2cWriteByte(lcdHandle, bits_low);
    lcdToggleEnable(bits_low);
}

// Clear screen
void lcdClear(void) {
    lcdByte(0x01, LCD_CMD);
    gpioDelay(2000); // Clearing display needs a longer 2ms delay
}

// Position cursor at a specific line address
void lcdLoc(int line) {
    lcdByte(line, LCD_CMD);
}

// Print string to current position
void lcdWriteString(const char *s) {
    while (*s) lcdByte(*s++, LCD_CHR);
}

// Initialize the LCD controller into 4-bit operational mode
void lcdInit() {
    lcdByte(0x33, LCD_CMD); // 8-bit initialization fallback
    lcdByte(0x32, LCD_CMD); // Set to 4-bit mode
    lcdByte(0x06, LCD_CMD); // Cursor direction: entry mode set
    lcdByte(0x0C, LCD_CMD); // Display On, Cursor Off, Blink Off
    lcdByte(0x28, LCD_CMD); // Function set: 2-line mode, 5x8 dots
    lcdClear();
}


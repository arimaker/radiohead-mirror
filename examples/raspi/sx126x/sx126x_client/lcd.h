// lcd.h
//
// Definitions for lcd support.
// Requires Pigpio GPIO library.
//(9/7/2026)   Contributed by Tilman Glötzner.

#ifndef LCD_H
#define LCD_H
#include <pigpio.h>

// LCD's I2C address
#define I2C_ADDR 0x27
#define I2C_BUS  1

// LCD Modes / Flags
#define LCD_CHR  1 // Mode - Sending data
#define LCD_CMD  0 // Mode - Sending command

// 20x4 Row Memory Map Addresses
#define LINE1  0x80 // Row 1
#define LINE2  0xC0 // Row 2
#define LINE3  0x94 // Row 3
#define LINE4  0xD4 // Row 4

#define LCD_BACKLIGHT   0x08  // On mask
#define ENABLE          0x04  // Enable pulse bit

extern int lcdHandle; // pigpio I2C handle

// Pulse the enable pin to latch data into the HD44780 controller

// Split 8-bit characters/commands into two 4-bit nibbles over I2C
void lcdByte(int bits, int mode);

// Clear screen
void lcdClear(void);

// Position cursor at a specific line address
void lcdLoc(int line);

// Print string to current position
void lcdWriteString(const char *s);

// Initialize the LCD controller into 4-bit operational mode
void lcdInit();
#endif

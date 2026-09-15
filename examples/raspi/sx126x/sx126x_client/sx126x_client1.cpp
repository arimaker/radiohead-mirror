// sx126x_client1.cpp
// -*- mode: C++ -*-
// Example app showing how to create a simple messaging client
// with the RH_SX126x class. RH_SX126x class does not provide for addressing or
// reliability, so you should only use it if you do not need the higher
// level messaging abilities.
// It is designed to work with a board running 2 SX126x, one acting as sender
// the other one as receiver. The reset line is shared across both SX126x.
// In addition, a lcd display can connected to the I2C bus.
//
// Requires Pigpio GPIO library. Install by downloading and compiling from
// http://abyz.me.uk/rpi/pigpio/, or install via command line with 
// "sudo apt install pigpio". To use, run "make" at the command line in 
// the folder where this source code resides. Then execute application with
// sudo ./sc126x_client1.
// Tested on Raspberry Pi 3 and 2 AI Thinker RA01s modules using the SX1268.

//(8/23/2026)   Contributed by Tilman Glötzner. Influenced by rf95_client by 
//              Bordy M.

#include <pigpio.h>
#include <lcd.h>
#include <string.h>
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

#include <RH_SX126x.h>

//Function Definitions
void sig_handler(int sig);

//Pin Definitions

#define SX126X_TX_RX_RESET_PIN 4 // RESET on GPIO4 so P1 connector pin #7

#define SX126X_TX_CS_PIN 27 // TX-Select on GPIO27, i.e. PI connector #13
#define SX126X_TX_BUSY_PIN 18 // TX-Busy on GPIO18, i.e. PI connector #12
#define SX126X_TX_IRQ_PIN 23 // TX-IRQ/DIO1 on GPIO23, i.e. PI connector #16

#define SX126X_RX_CS_PIN 25 // RX-Select on GPIO25, i.e. PI connector #22
#define SX126X_RX_BUSY_PIN 17 // RX-Busy on GPIO17, i.e. PI connector #11
#define SX126X_RX_IRQ_PIN 8 // TX-IRQ/DIO1 on GPIO8, i.e. PI connector #24

//Client and Server Addresses
#define CLIENT_ADDRESS 1
#define SERVER_ADDRESS 2

//RFM95 Configuration
#ifdef EUROPE
#define SX126X_FREQUENCY 434.50
#else
#define SX126X_FREQUENCY 434.50
#endif
#define SX126X_TXPOWER 2

// Instance of the radio driver for the tx radio
RH_SX126x sx126x_tx(SX126X_TX_CS_PIN, SX126X_TX_IRQ_PIN,SX126X_TX_BUSY_PIN,SX126X_TX_RX_RESET_PIN);
RH_SX126x sx126x_rx(SX126X_RX_CS_PIN, SX126X_RX_IRQ_PIN,SX126X_RX_BUSY_PIN,SX126X_TX_RX_RESET_PIN);

//Flag for Ctrl-C
int flag = 0;

//Main Function
int main (int argc, const char* argv[] )
{
	 bool rc = 0;
	 printf( "\n\nRPI gpioInitialise.\n" );
	 if (gpioInitialise()<0)
	 {
		 printf( "\n\nRPI sx126_client startup Failed.\n" );
		 return 1;
	 }

	 gpioSetSignalFunc(2, sig_handler); //2 is SIGINT. Ctrl+C will cause signal.

	lcdHandle = i2cOpen(I2C_BUS, I2C_ADDR, 0);
    	if (lcdHandle < 0) {
       		printf("Failed to open I2C bus! Error code: %d", lcdHandle);
        	gpioTerminate();
        	return 1;
    	}
	
	sx126x_rx.setBusyTimeout(70);
	sx126x_tx.setBusyTimeout(70);

	 if (!sx126x_rx.init())
	 {
		 printf( "\n\nSX126x driver (rx) failed to initialize.\n\n" );

	 }

	 if (!sx126x_tx.init(false))
	 {
		 printf( "\n\nSX126x driver (tx) failed to initialize.\n\n" );

	 }
 
	 printf( "\nRPI sx126x_client startup OK.\n" );
	 printf( "\nRPI GPIO settings:\n" );
	 printf("CS(TX)-> GPIO %d\n", (uint8_t) SX126X_TX_CS_PIN);
	 printf("IRQ(TX)-> GPIO %d\n", (uint8_t) SX126X_TX_IRQ_PIN);
	 printf("BUSY(TX)-> GPIO %d\n", (uint8_t) SX126X_TX_BUSY_PIN);
	 printf("RESET-> GPIO %d\n", (uint8_t) SX126X_TX_RX_RESET_PIN);
	 printf("CS(RX)-> GPIO %d\n", (uint8_t) SX126X_RX_CS_PIN);
	 printf("IRQ(RX)-> GPIO %d\n", (uint8_t) SX126X_RX_IRQ_PIN);
	 printf("BUSY(RX)-> GPIO %d\n", (uint8_t) SX126X_RX_BUSY_PIN);
	 gpioDelay(4000000);

	 lcdLoc(LINE1);
	 lcdWriteString("SX126x_tx goes to idle mode."); 
	 sx126x_tx.setModeIdle();
	 lcdLoc(LINE2);
 
	 lcdWriteString("SX126x_rx goes to idle mode." );
	 sx126x_rx.setModeIdle();
	 gpioDelay(4000000);


  	/* Begin Manager/Driver settings code */
  	printf("\nSX126x Settings:\n");
  	printf("Frequency= %d MHz\n", (uint16_t) SX126X_FREQUENCY);
  	printf("Power= %d\n", (uint8_t) SX126X_TXPOWER);
  	printf("Client(This) Address= %d\n", CLIENT_ADDRESS);
  	printf("Server Address= %d\n", SERVER_ADDRESS);
  	sx126x_tx.setTxPower(SX126X_TXPOWER);
  	sx126x_tx.setFrequency(SX126X_FREQUENCY);
  	sx126x_tx.setThisAddress(CLIENT_ADDRESS);
  	//sx126x_tx.setHeaderFrom(CLIENT_ADDRESS);
  	sx126x_tx.setHeaderTo(SERVER_ADDRESS);
  	sx126x_tx.setModemConfig(RH_SX126x::LoRa_Bw125Cr45Sf128);
  	sx126x_rx.setTxPower(SX126X_TXPOWER);
  	sx126x_rx.setFrequency(SX126X_FREQUENCY);
  	sx126x_rx.setThisAddress(SERVER_ADDRESS);
  	//sx126x_rx.setHeaderFrom(SERVER_ADDRESS);
	sx126x_rx.setHeaderTo(CLIENT_ADDRESS);
  	sx126x_rx.setModemConfig(RH_SX126x::LoRa_Bw125Cr45Sf128);
 	// sx126x_rx.setModeRx();

	lcdInit();
  	/* End Manager/Driver settings code */

  	/* Begin Datagram Client Code */
	int count = 0;
	sx126x_rx.setModeRx(); 
  	while(!flag)
  	{
		char textbuf[20];
		lcdClear();
		lcdLoc(LINE1);
		snprintf(textbuf,20,"Sending @ %6.2fMhz",SX126X_FREQUENCY);
	 	lcdWriteString(textbuf);
    		Serial.println(textbuf);
    		uint8_t data[] = "Hello World!( )";
		data[sizeof(data)-3] = count + 48;
    		sx126x_tx.send(data, sizeof(data));
    		sx126x_tx.waitPacketSent();
		count++;
		count %= 10;    	
		// Now wait for a reply
    		    		
    	uint8_t buf[RH_SX126x_MAX_MESSAGE_LEN];
    	uint8_t len = sizeof(buf);

		if (sx126x_rx.waitAvailableTimeout(3000))
   		{
      		// Should be a reply message for us now
      		if (sx126x_rx.recv(buf, &len))
      		{
				lcdLoc(LINE2);
				lcdWriteString((char*)buf);
          		Serial.print("Received: ");
          		Serial.println((char*)buf);
      		}
      		else
      		{
				lcdLoc(LINE2);
				lcdWriteString("Recv failed.");
        		Serial.println("recv failed.");
      		}
    	}
    	else
    	{
			lcdLoc(LINE2);
			lcdWriteString("No Reply.");
      		Serial.println("No Reply.");
    	}
    	gpioDelay(400000);
  	}
	lcdClear();
  	Serial.print( "sx126x_client1 Tester terminated.\n" );
	lcdLoc(LINE1);
	lcdWriteString("  sx126x_client1");
	lcdLoc(LINE2);
	lcdWriteString("    terminated.");
	i2cClose(lcdHandle);
  	gpioTerminate();

  	return 0;
}

void sig_handler(int sig)
{
  flag=1;
}


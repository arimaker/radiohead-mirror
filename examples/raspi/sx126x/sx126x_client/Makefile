# Makefile
# Example for SX_126x on Raspberry Pi
# Requires pigpio to be installed: http://abyz.me.uk/rpi/pigpio/


CROSSCOMPILER=$(shell if [ -z `which 'arm-linux-gnueabihf-g++'` ]; then echo "no"; else echo "yes"; fi)
ifeq ($(CROSSCOMPILER),yes)
CC            = arm-linux-gnueabihf-g++
CFLAGS        = -DRASPBERRY_PI -DRH_USE_MUTEX -pthread 
RADIOHEADBASE = ../../../..
PIGPIOBASE    = ../../../../../pigpio/
SHARED        = ../shared/
INCLUDE       = -I$(RADIOHEADBASE) -I$(PIGPIOBASE) -I$(SHARED) -I.
LIBS          = -lpigpio -lrt -L$(PIGPIOBASE) -lpthread  -D_REENTRANT
else
CC            = g++
CFLAGS        = -DRASPBERRY_PI -DRH_USE_MUTEX -pthread
RADIOHEADBASE = ../../../..
PIGPIOBASE    = ../../../../../pigpio/
SHARED        = ../shared/
INCLUDE       = -I$(RADIOHEADBASE) -I$(PIGPIOBASE) -I$(SHARED) -I.
LIBS          = -lpigpio -lrt -L$(PIGPIOBASE) -lpthread  -D_REENTRANT
endif

ifeq ($(REGION),Europe)
CFLAGS += -DEUROPE
endif

ifeq ($(DEBUG),1)
CFLAGS += -g3
endif

all: sx126x_client1

lcd.o: lcd.cpp
	$(CC) $(CFLAGS) -c $(INCLUDE) $<

RasPi.o: $(RADIOHEADBASE)/RHutil_pigpio/RasPi.cpp
	$(CC) $(CFLAGS) -c $(RADIOHEADBASE)/RHutil_pigpio/RasPi.cpp $(INCLUDE)

help_functions.o: $(SHARED)/help_functions.cpp
	$(CC) $(CFLAGS) -c $(INCLUDE) $<
	
sx126x_client1.o: sx126x_client1.cpp 
	$(CC) $(CFLAGS) -c $(INCLUDE) $<
	
sx1268_client2.o: sx1268_client2.cpp 
	$(CC) $(CFLAGS) -c $(INCLUDE) $<

RH_SX126x.o: $(RADIOHEADBASE)/RH_SX126x.cpp
	$(CC) $(CFLAGS) -c $(INCLUDE) $<

RHDatagram.o: $(RADIOHEADBASE)/RHDatagram.cpp
	$(CC) $(CFLAGS) -c $(INCLUDE) $<

RHHardwareSPI.o: $(RADIOHEADBASE)/RHHardwareSPI.cpp
	$(CC) $(CFLAGS) -c $(INCLUDE) $<

RHSPIDriver.o: $(RADIOHEADBASE)/RHSPIDriver.cpp
	$(CC) $(CFLAGS) -c $(INCLUDE) $<

RHGenericDriver.o: $(RADIOHEADBASE)/RHGenericDriver.cpp
	$(CC) $(CFLAGS) -c $(INCLUDE) $<

RHGenericSPI.o: $(RADIOHEADBASE)/RHGenericSPI.cpp
	$(CC) $(CFLAGS) -c $(INCLUDE) $<

sx126x_client1: sx126x_client1.o RH_SX126x.o RHDatagram.o RasPi.o RHHardwareSPI.o RHSPIDriver.o RHGenericDriver.o RHGenericSPI.o lcd.o
	$(CC) $^ $(LIBS) -o sx126x_client1

clean:
	rm -rf *.o sx126x_client1 sx126x_client2

deploy: sx126x_client1
	sshpass -p"$(PASSWD)" scp sx126x_client1 pi@$(HOST):/home/pi

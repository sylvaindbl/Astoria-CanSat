import board
import busio
import digitalio
import time

import adafruit_rfm9x

# init radio 
RADIO_FREQ_MHZ = 433.9
CS = digitalio.DigitalInOut(board.GP5)
RESET = digitalio.DigitalInOut(board.GP3)
spi = busio.SPI(board.GP6, MOSI=board.GP7, MISO=board.GP4)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23

#init led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("Waiting for packets...")

while True:
    packet = rfm9x.receive()
    
    if packet is None:
        led.value = True
        led.value = False
    else:
        packet_text = str(packet, "ascii")
        print("{0}".format(packet_text))


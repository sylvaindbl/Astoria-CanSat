import board
print("board")
import busio
print("busio")
import digitalio
print("digitalio")

import adafruit_rfm9x
print('rfm')

# init radio 
RADIO_FREQ_MHZ = 434.4
CS = digitalio.DigitalInOut(board.GP5)
RESET = digitalio.DigitalInOut(board.GP3)
spi = busio.SPI(board.GP6, MOSI=board.GP7, MISO=board.GP4)
#spi = busio.SPI(board.GP6, MOSI=board.GP4, MISO=board.GP7)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23

rfm9x.send(bytes("Hello world!\r\n", "utf-8"))
print(bytes("Hello world!\r\n", "utf-8"))
print("Sent Hello World message!")

print("Waiting for packets...")

while True:
    packet = rfm9x.receive()
    
    if packet is None:
        # Packet has not been received
        print("Received nothing! Listening again...")
    else:
        print("Received (raw bytes): {0}".format(packet))
        packet_text = str(packet, "ascii")
        print("Received (ASCII): {0}".format(packet_text))
        rssi = rfm9x.last_rssi
        print("Received signal strength: {0} dB".format(rssi))

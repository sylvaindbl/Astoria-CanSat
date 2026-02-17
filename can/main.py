import board
import busio
import digitalio
import time

import adafruit_rfm9x
import adafruit_bme680
import adafruit_bno055
import adafruit_tsl2591
import adafruit_gps
import adafruit_sdcard
import storage

#init led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# init radio 
RADIO_FREQ_MHZ = 434.4
CS = digitalio.DigitalInOut(board.GP5)
RESET = digitalio.DigitalInOut(board.GP3)
spi = busio.SPI(board.GP6, MOSI=board.GP7, MISO=board.GP4)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23

#init bme and tsl
i2c_bme = busio.I2C(board.GP9, board.GP8)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c_bme, 0x77)
bme680.sea_level_pressure = 1013.25
temperature_offset = -5
tsl = adafruit_tsl2591.TSL2591(i2c_bme, 0x29)

#init buzzer
pin_gp15 = board.GP15
buzzer = digitalio.DigitalInOut(pin_gp15)
buzzer.direction = digitalio.Direction.OUTPUT

#init sd video
pin_gp20 = board.GP20
sd_video = digitalio.DigitalInOut(pin_gp20)
sd_video.direction = digitalio.Direction.OUTPUT

#init video
pin_gp21 = board.GP21
video = digitalio.DigitalInOut(pin_gp21)
video.direction = digitalio.Direction.OUTPUT

#init bno055
bno_i2c = busio.I2C(board.GP19, board.GP18)
bno = adafruit_bno055.BNO055_I2C(bno_i2c)
last_val = 0xFFFF

#init gps
uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)  
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
last_print = time.monotonic()

#init sd
SD_CS = board.GP13
sd_spi = busio.SPI(board.GP10, board.GP11, board.GP12)
sd_cs = digitalio.DigitalInOut(SD_CS)
sdcard = adafruit_sdcard.SDCard(sd_spi, sd_cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

x=0

# Récupérer le temps de démarrage
start_time = time.time()

while True:
    try:
        # Récupérer le temps actuel
        current_time = time.time()
        elapsed_time = current_time - start_time
        time_42="{:.0f}".format(elapsed_time)
        
        temp="%0.1f" % (bme680.temperature + temperature_offset)
        gas="%d" % bme680.gas
        humi="%0.1f" % bme680.relative_humidity
        pres="%0.3f" % bme680.pressure
        alti="%0.2f" % bme680.altitude
        acc="{}".format(bno.acceleration)
        mag="{}".format(bno.magnetic)
        gyr="{}".format(bno.gyro)
        
        lux="{0}".format(tsl.lux)
        infr="{0}".format(tsl.infrared)
        visi="{0}".format(tsl.visible)
        
    
        gps.update()
        if gps.has_fix:
            lat="{0:.6f}".format(gps.latitude)
            lon="{0:.6f}".format(gps.longitude)
            if gps.altitude_m is not None:
                alt="{}".format(gps.altitude_m)
        else:
            lat=0
            lon=0
            alt=0
    
        msg = f"{time_42}, {pres}, {temp}, {alti}, {humi}, {gas}, {lux}, {infr}, {visi}, {acc}, {mag}, {gyr}, {lat}, {lon}, {alt}"
        print(msg)
        rfm9x.send(bytes(msg, "utf-8"))
        print("sent packet")
    
        with open("/sd/temperature.txt", "a") as f:
            led.value = True
            sd_send=f"\n {time_42}, {pres}, {temp}, {alti}, {humi}, {gas}, {lux}, {infr}, {visi}, {acc}, {mag}, {gyr}, {lat}, {lon}, {alt}"
            print(sd_send)
            f.write(sd_send)
            led.value = False
        print("sd")
    
        accel=acc.split(",")
        try:
            a_x=accel[1]
            ax=float(a_x)
            print(ax)
        except:
            print("ax")
        try:
            a_y=accel[2]
            ya=a_y.replace(')', '')
            ay=float(ya)
            print(ay)
        except:
            print("ay")
        try:
            a_z=accel[0]
            za=a_z.replace('(', '')
            az=float(za)
        except:
            print(az)
        
        if ax>30 or ax<-30 or az>30 or az<-30 or ay>30 or ay<-30 :
            break
        
        """alti_bme=float(alti)
        if alti_bme>800:
            break
        alt_gps=float(alt)
        if alt_gps>800:
            break"""
            
    except:
        print("bug")
        
    x=x+1
    print(x)
    if x>5:
        break
    
    
    time.sleep(1)
    
#switch
print("switch1")
video.value=True
sd_video.value=True
msg=("switch")
rfm9x.send(bytes(msg, "utf-8"))
sd_video.value=False
y=0

while True:
    try:
        # Récupérer le temps actuel
        current_time = time.time()
        elapsed_time = current_time - start_time
        time_42="{:.0f}".format(elapsed_time)
        
        temp="%0.1f" % (bme680.temperature + temperature_offset)
        gas="%d" % bme680.gas
        humi="%0.1f" % bme680.relative_humidity
        pres="%0.3f" % bme680.pressure
        alti="%0.2f" % bme680.altitude
        acc="{}".format(bno.acceleration)
        mag="{}".format(bno.magnetic)
        gyr="{}".format(bno.gyro)
        lux="{0}".format(tsl.lux)
        infr="{0}".format(tsl.infrared)
        visi="{0}".format(tsl.visible)
    
        gps.update()
        if gps.has_fix:
            lat="{0:.6f}".format(gps.latitude)
            lon="{0:.6f}".format(gps.longitude)
            if gps.altitude_m is not None:
                alt="{}".format(gps.altitude_m)
        else:
            lat=0
            lon=0
            alt=0
    
        msg = f"{time_42}, {pres}, {temp}, {alti}, {humi}, {gas}, {lux}, {infr}, {visi}, {acc}, {mag}, {gyr}, {lat}, {lon}, {alt}"
        print(msg)
        rfm9x.send(bytes(msg, "utf-8"))
        print("sent packet")
    
        with open("/sd/temperature.txt", "a") as f:
            led.value = True
            sd_send=f"\n {time_42}, {pres}, {temp}, {alti}, {humi}, {gas}, {lux}, {infr}, {visi}, {acc}, {mag}, {gyr}, {lat}, {lon}, {alt}"
            print(sd_send)
            f.write(sd_send)
            led.value = False
        print("sd")
            
    except:
        print("bug")
        
    y=y+1
    print(y)
    if y>10:
        break
    
    time.sleep(0.3)
    
print("switch2")
sd_video.value=True
time.sleep(1)
sd_video.value=False
time.sleep(1)
video.value=True


while True:
    buzzer.value=True
    time.sleep(0.4)
    buzzer.value=False
    time.sleep(0.4)
    
    buzzer.value=True
    time.sleep(0.4)
    buzzer.value=False
    time.sleep(0.4)
    
    buzzer.value=True
    time.sleep(0.2)
    buzzer.value=False
    time.sleep(0.2)
    
    buzzer.value=True
    time.sleep(0.2)
    buzzer.value=False
    time.sleep(0.2)
    
    buzzer.value=True
    time.sleep(0.4)
    buzzer.value=False
    time.sleep(0.4)





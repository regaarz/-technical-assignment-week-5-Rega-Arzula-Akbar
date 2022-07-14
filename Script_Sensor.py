import time  
import board 
import adafruit_dht 
import psutil 
for proc in psutil.process_iter(): 
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei': 
        proc.kill()
sensor = Adafruit_DHT.DHT11 # 
DHT_PIN = 4
while True: 
    try:
        humidity, temperature = Adafruit_DHT. read(sensor, DHT_PIN) 
        print("Temperature: {}*C Humidity: {}".format(temperature, humidity))
    except RuntimeError as error: 
        print(error.args[0]) 
        time.sleep(1.0) 
        continue
    except Exception as error:  
        sensor.exit()
        raise error
    time.sleep(1.0) 

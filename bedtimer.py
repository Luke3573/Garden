import RPi.GPIO as GPIO
import serial
import Adafruit_DHT
import os
import datetime
import time
from subprocess import call
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
GPIO.setup(17, GPIO.OUT)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 14

def Watering():

    if True:

        current_time = datetime.datetime.now()
        hour = current_time.hour
        minute = current_time.minute

        GPIO.output(17, 1)
        print("start")
        print(hour, minute)

        temp()



def Stop_watering():

    if True:

        current_time = datetime.datetime.now()
        hour = current_time.hour
        minute = current_time.minute

        GPIO.output(17,0)
        print("stop")
        print(hour, minute)

        scheduler()



def temp():

    if True:
        current_time = datetime.datetime.now()
        hour = current_time.hour
        minute = current_time.minute

        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        time.sleep(1)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            temperature = temperature
            humidity = humidity
            time.sleep(1)
            print(hour, minute)
            scheduler()
        else:
            temperature = "FLT"
            humidity = "FLT"
            print(hour, minute)
            print(temperature, humidity)
            time.sleep(3);
            scheduler()

def scheduler():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute

    if hour == 6 and minute == 30:
        time.sleep(20)
        Watering()

    elif hour == 7 and minute == 0:
        time.sleep(20)
        Stop_watering()

    elif hour == 16 and minute == 0:
        time.sleep(20)
        Watering()

    elif hour == 16 and minute == 30:
        time.sleep(20)
        Stop_watering()

    else:
        time.sleep(20)
        scheduler()


def RUN():
    print("started")
    temp()
    scheduler()
    print("finished")

RUN()
print("finished main")


def main():
    import RPi.GPIO as GPIO
    import pyrebase
    import time
    import serial
    import Adafruit_DHT
    #        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
    GPIO.setup(17, GPIO.OUT)
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 14
    config1 = {
        "apiKey": "AIzaSyB_2lt7J9iazmvtS8Wxw_GTH_Qo37HAT3c",
        "authDomain": "home-garden-25b17.firebaseapp.com",
        "databaseURL": "https://home-garden-25b17.firebaseio.com/",
        "storageBucket": "GMS.appspot.com"
    }

    firebase1 = pyrebase.initialize_app(config1)

    if True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        time.sleep(1)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            temperature = temperature
            humidity = humidity
            time.sleep(1)
        else:
            temperature = "FLT"
            humidity = "FLT"
            time.sleep(3);

    if True:
        database = firebase1.database()
        gardenMonitoring = database.child("GMS")
        valve = gardenMonitoring.child("valveStatus").get().val()
        global valveStatus
        valveStatus = valve

        database = firebase1.database()
        gardenMonitoring.child("GMS").child("temperature").set(temperature)

        # database = firebase1.database()
        # gardenMonitoring.child("GMS").child("moisture").set(bedMoisture)

        database = firebase1.database()
        gardenMonitoring.child("GMS").child("humidity").set(humidity)

        # database = firebase1.database()
        # gardenMonitoring.child("GMS").child("bedBatt").set(bedBatt)
        global systemActive
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("systemActive").set(systemActive)

        time.sleep(10)

        else:
        main()
    if valveStatus == "1":
        GPIO.output(17, 1)
        systemActive = "1"
        #                print ("run")
        main()
    elif valveStatus == "0":
        GPIO.output(17, 0)
        systemActive = "0"
        #               print ("stop")

        main()
    else:
        time.sleep(2)
        main()

def sched():
#    *********time call**********
        hour = time.time()
        print(hour)
        if hour == time1 && minute == time2:
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("valveStatus").set("1")
        
    else:
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("valveStatus").set("1")
        main()

sensor = 0
temperature = 1
humidity = 1
level = 1
bedMoisture = 1
systemActive = 0
valveStatus = 0
fans = 0
# print ("started")
main()
# read()
# globals()


def main():
    import RPi.GPIO as GPIO
    import pyrebase
    import time
    import serial
    from PiicoDev_TMP117 import PiicoDev_TMP117
    from PiicoDev_Unified import sleep_ms

    sensorA = PiicoDev_TMP117(asw=[1, 0, 0, 0])
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
    GPIO.setup(17, GPIO.OUT)
    config1 = {
        "apiKey": "AIzaSyB_2lt7J9iazmvtS8Wxw_GTH_Qo37HAT3c",
        "authDomain": "home-garden-25b17.firebaseapp.com",
        "databaseURL": "https://home-garden-25b17.firebaseio.com/",
        "storageBucket": "GMS.appspot.com"
    }

    firebase1 = pyrebase.initialize_app(config1)

    if True:
        tempA = sensorA.readTempC()
        time.sleep(1)
        if tempA is not None:
            Temp = ("{:.2f}°C".format(tempA))
            temperature = Temp
            time.sleep(1)
        else:
            temperature = "FLT"
            time.sleep(3);

    if True:
        database = firebase1.database()
        gardenMonitoring = database.child("GMS")
        valve = gardenMonitoring.child("valveStatus").get().val()
        global valveStatus
        valveStatus = valve

        database = firebase1.database()
        gardenMonitoring.child("GMS").child("temperature").set(temperature)

        global systemActive
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("systemActive").set(systemActive)

        time.sleep(10)

        else:
        main()
    if valveStatus == "1":
        GPIO.output(17, 1)
        systemActive = "1"
        main()
    elif valveStatus == "0":
        GPIO.output(17, 0)
        systemActive = "0"

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
level = 1
bedMoisture = 1
systemActive = 0
valveStatus = 0
fans = 0
main()

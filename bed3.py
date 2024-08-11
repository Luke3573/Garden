def main():
    print ("start")
    import RPi.GPIO as GPIO
    from urllib3 import disable_warnings
    from urllib3.exceptions import InsecureRequestWarning
    disable_warnings(InsecureRequestWarning)
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
    print ("firebase get")
    if True:
        tempA = sensorA.readTempC()
        time.sleep(1)
        print ("temp read")
        if tempA is not None:
            Temp = ("{:.2f}°C".format(tempA))
            temperature = Temp
            time.sleep(1)
            print ("temp read yes")
        else:
            temperature = "FLT"
            time.sleep(3);
            print ("temp read no")

    if True:
        database = firebase1.database()
        gardenMonitoring = database.child("GMS")
        valve = gardenMonitoring.child("valveStatus").get().val()
        global valveStatus
        valveStatus = valve
        print ("valve stat get")

        database = firebase1.database()
        gardenMonitoring.child("GMS").child("temperature").set(temperature)
        print ("temp set")
        global systemActive
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("systemActive").set(systemActive)
        print ("set system")
        time.sleep(10)

    else:
        print ("data fail")
        main()

    if valveStatus == "1":
        GPIO.output(17, 1)
        systemActive = "1"
        print ("set valve 1")
  #      main()
    elif valveStatus == "0":
        GPIO.output(17, 0)
        systemActive = "0"
        print ("set valve 0")

 #       main()
    else:
        time.sleep(2)
        print ("set valve fail")
        main()


    if True:
        current_time = time.time()
        local_time = time.localtime(current_time)

        hour = local_time.tm_hour
        minute = local_time.tm_min

        if hour == 23 and minute == 55:
            call("clear", shell=True)
            call(" sudo sh -c 'echo 1 >  /proc/sys/vm/drop_caches' ", shell=True)

            time.sleep(10)
            main()

        else:

            main()

    else:
        main()

def sched():
#    *********time call**********
        hour = time.time()
        print(hour)
        if hour == time1 :
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




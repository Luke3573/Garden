def main():
    import RPi.GPIO as GPIO  # import the RPi.GPIO module to allow us use the board GPIO pins.
    from gpiozero import CPUTemperature
    from subprocess import call
    import pyrebase
    import time

    config1 = {
        "apiKey": "AIzaSyB_2lt7J9iazmvtS8Wxw_GTH_Qo37HAT3c",
        "authDomain": "home-garden-25b17.firebaseapp.com",
        "databaseURL": "https://home-garden-25b17.firebaseio.com/",
        "storageBucket": "GMS.appspot.com"
    }

    firebase1 = pyrebase.initialize_app(config1)  


    if True:

        database = firebase1.database() 
        gardenMonitoring = database.child("GMS") 
        shut = gardenMonitoring.child("shutdown").get().val()
        global shutdown
        shutdown = shut

        cpu = CPUTemperature()

        database = firebase1.database()
        gardenMonitoring.child("GMS").child("ControlTemp").set(cpu.temperature)
#        print(cpu.temperature)
        time.sleep(10)

    else:
        main()

    if shutdown == "1":
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("shutdown").set("0")
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("ControlTemp").set("0")
#        database = firebase1.database()
 #       gardenMonitoring.child("GMS").child("shedBatt").set("0")
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("tankLevel").set("0")
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("shedTemp").set("0")
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("fans").set("2")
        database = firebase1.database()
        call("sudo shutdown now ", shell=True)

    elif shutdown == "0":
        main()

    elif shutdown == "3":
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("shutdown").set("0")
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("ControlTemp").set("0")
 #       database = firebase1.database()
#        gardenMonitoring.child("GMS").child("battery").set("0")
   #     database = firebase1.database()
  #      gardenMonitoring.child("GMS").child("bed_battery").set("0")
#        database = firebase1.database()
 #       gardenMonitoring.child("GMS").child("humidity").set("0")
  #      database = firebase1.database()
   #     gardenMonitoring.child("GMS").child("moisture").set("0")
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("tankLevel").set("0")
 #       database = firebase1.database()
  #      gardenMonitoring.child("GMS").child("temperature").set("0")
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("fans").set("0")
        database = firebase1.database()
        gardenMonitoring.child("GMS").child("valveStatus").set("2")
        call("sudo shutdown now -r", shell=True)

        main()
    else:
        time.sleep(2)
        main()


sensor = 0
temperature = 1
humidity = 1
level = 1
bedMoisture = 1
systemActive = 0
valveStatus = 0
fans = 0
print("started")
main()
read()
globals()

		


def main():
        import RPi.GPIO as GPIO                                                                         
        import pyrebase
        import time
        import serial
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        config1 = {                                                              
                "apiKey":"AIzaSyB_2lt7J9iazmvtS8Wxw_GTH_Qo37HAT3c",
                "authDomain": "home-garden-25b17.firebaseapp.com",
                "databaseURL": "https://home-garden-25b17.firebaseio.com/",
                "storageBucket": "GMS.appspot.com"
        }

        firebase1 = pyrebase.initialize_app(config1) 
        if True:

                def request_reading():
                        line = ser.readline().decode('utf-8').rstrip()
                        parsed = line.split(',')
                        parsed = [x.rstrip() for x in parsed]
                        bedBatt = (parsed[0])
                        temperature = (parsed[1])
                        level = (parsed[2])
                        fanStatus = (parsed[3])
                       


                        return  bedBatt, temperature, level, fanStatus,

                bedBatt, temperature, level, fanStatus, = request_reading()

        else:
                main()

        if True:
                database = firebase1.database()
                gardenMonitoring = database.child("GMS")
                fan = gardenMonitoring.child("fans").get().val()
                global fans
                fans = fan

                database = firebase1.database()
                gardenMonitoring.child("GMS").child("shedTemp").set(temperature)

                database = firebase1.database()
                gardenMonitoring.child("GMS").child("tankLevel").set(level)

#                database = firebase1.database()
 #               gardenMonitoring.child("GMS").child("shedBatt").set(bedBatt)

                database = firebase1.database()
                gardenMonitoring.child("GMS").child("fanStatus").set(fanStatus)

                time.sleep(30)
        else:
                main()
        
        if fans == "1":
                GPIO.output (19,1)
                main()
        elif fans == "0":
                GPIO.output (19,0)
                main()
        else:
                time.sleep(2)
                main()






sensor = 0
temperature = 1
humidity = 1
level = 1
fans = 0
print ("started")
main()
read()
globals()
  

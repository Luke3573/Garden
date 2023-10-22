
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
                        humidity = (parsed[1])
                        temperature = (parsed[2])
                        bedMoisture = (parsed[3])
                        systemActive = (parsed[4])


                        return  bedBatt, humidity, temperature, bedMoisture, systemActive,

                bedBatt, humidity, temperature, bedMoisture, systemActive, = request_reading()

        else:
                main()

        if True:

                database = firebase1.database()  
                gardenMonitoring = database.child("GMS")   
                valve = gardenMonitoring.child("valveStatus").get().val()
                global valveStatus
                valveStatus = valve

                database = firebase1.database()
                gardenMonitoring.child("GMS").child("outTemp").set(temperature)
				
                database = firebase1.database()
                gardenMonitoring.child("GMS").child("moisture").set(bedMoisture)
				
                database = firebase1.database()
                gardenMonitoring.child("GMS").child("humidity").set(humidity)

                database = firebase1.database()
                gardenMonitoring.child("GMS").child("bedBatt").set(bedBatt)

                database = firebase1.database()
                gardenMonitoring.child("GMS").child("systemActive").set(systemActive)

                time.sleep(2)
        else:
                main()
        if valveStatus == "1":
                GPIO.output(4, 1)
				
        elif valveStatus == "0":
                GPIO.output(4, 0)
				
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
print ("started")
main()
read()
globals()
  

        def main():

                def request_reading():
                        #if (info):
                        reading = bus.read_i2c_block_data(SLAVE_ADDRESS, 0, 6)

                        bedBatt = reading[0]
                        tankBatt = reading[1]
                        humidity = reading[2]
                        temperature = reading[3]
                        bedMoisture = reading[4]
                        percentage = reading[5]


                        #       print ("bedBatt")
                        #      print (bedBatt)
                        #     print (tankBatt)
                        return  bedBatt , tankBatt , humidity, temperature, bedMoisture, percentage

                bedBatt, tankBatt, humidity, temperature, bedMoisture, percentage = request_reading()
               # tankBatt = request_reading()
               # humidity = request_reading()
               # temperature = request_reading()
               # bedMoisture = request_reading()
               # percentage = request_reading()

        if True:
                # the beginning of the main program.
                database = firebase1.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
                gardenMonitoring = database.child(
                        "GMS")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
                motor_state = gardenMonitoring.child("motor_state").get().val()

                print (motor_state)

                database = firebase1.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
                gardenMonitoring = database.child(
                        "GMS")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
                pi_state = gardenMonitoring.child("pi_state").get().val()
                print (pi_state)

                database = firebase1.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
                gardenMonitoring = database.child(
                        "GMS")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
                update = gardenMonitoring.child("update").get().val()
                print (update)

                database = firebase1.database()

                gardenMonitoring.child("GMS").child("temperature").set(temperature)
                print (temperature)



                        database = firebase1.database()
                        gardenMonitoring.child("GMS").child("tankLevel").set(percentage)

                        database = firebase1.database()
                        gardenMonitoring.child("GMS").child("moisture").set(bedMoisture)
                        database = firebase1.database()
                        gardenMonitoring.child("GMS").child("humidity").set(humidity)
                        database = firebase1.database()
                        gardenMonitoring.child("GMS").child("bed_battery").set(bedBatt)
                        database = firebase1.database()
                        gardenMonitoring.child("GMS").child("tank_battery").set(tankBatt)
                        main()
                else:
                        main()
              #  if false:
                       # main()
# import RPi.GPIO as GPIO                                                                         #import the RPi.GPIO module to allow us use the board GPIO pins.
import pyrebase
import smbus
import time

temp = 1  # import the time modulde to allow us do the delay stuff.
bus = smbus.SMBus(1)
time.sleep(2)  # wait here to avoid 121 IO Error
SLAVE_ADDRESS = 0x04
config1 = {
       # define a dictionary named config with several key-value pairs that configure the connection to the database.
          "apiKey": "AIzaSyB_2lt7J9iazmvtS8Wxw_GTH_Qo37HAT3c",
          "authDomain": "home-garden-25b17.firebaseapp.com",
          "databaseURL": "https://home-garden-25b17.firebaseio.com/",
          "storageBucket": "GMS.appspot.com"
        }

 firebase1 = pyrebase.initialize_app(config1)  # initialize the communication with the "firebase" servers using the previous config data.

temperature = 1
humidity = 1
percentage = 1
bedMoisture = 1
main()




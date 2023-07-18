import pyrebase
import time

time.sleep(1)  # wait here to avoid 121 IO Error
teamtotal = 0
LukeH = {
       # define a dictionary named config with several key-value pairs that configure the connection to the database.
          "apiKey": "AIzaSyDNDmXlRagasLk36aHuRYKsOoE_dBrIEqA",
          "authDomain": "bhprecignition.firebaseapp.com",
          "databaseURL": "https://bhprecignition.firebaseio.com",
          "storageBucket": "LukeHaeusler.appspot.com"
        }
PaulR = {
       # define a dictionary named config with several key-value pairs that configure the connection to the database.
          "apiKey": "AIzaSyDNDmXlRagasLk36aHuRYKsOoE_dBrIEqA",
          "authDomain": "bhprecignition.firebaseapp.com",
          "databaseURL": "https://bhprecignition.firebaseio.com",
          "storageBucket": "PaulRoff.appspot.com"
        }
ThomasR = {
       # define a dictionary named config with several key-value pairs that configure the connection to the database.
          "apiKey": "AIzaSyDNDmXlRagasLk36aHuRYKsOoE_dBrIEqA",
          "authDomain": "bhprecignition.firebaseapp.com",
          "databaseURL": "https://bhprecignition.firebaseio.com",
          "storageBucket": "ThomasRoff.appspot.com"
        }
LukeG = {
       # define a dictionary named config with several key-value pairs that configure the connection to the database.
          "apiKey": "AIzaSyDNDmXlRagasLk36aHuRYKsOoE_dBrIEqA",
          "authDomain": "bhprecignition.firebaseapp.com",
          "databaseURL": "https://bhprecignition.firebaseio.com",
          "storageBucket": "LukeGrant.appspot.com"
        }
CaralynH = {
       # define a dictionary named config with several key-value pairs that configure the connection to the database.
          "apiKey": "AIzaSyDNDmXlRagasLk36aHuRYKsOoE_dBrIEqA",
          "authDomain": "bhprecignition.firebaseapp.com",
          "databaseURL": "https://bhprecignition.firebaseio.com",
          "storageBucket": "CaralynHauser.appspot.com"
        }
AlexP = {
       # define a dictionary named config with several key-value pairs that configure the connection to the database.
          "apiKey": "AIzaSyDNDmXlRagasLk36aHuRYKsOoE_dBrIEqA",
          "authDomain": "bhprecignition.firebaseapp.com",
          "databaseURL": "https://bhprecignition.firebaseio.com",
          "storageBucket": "AlexPerez.appspot.com"
        }
RichardD = {
       # define a dictionary named config with several key-value pairs that configure the connection to the database.
          "apiKey": "AIzaSyDNDmXlRagasLk36aHuRYKsOoE_dBrIEqA",
          "authDomain": "bhprecignition.firebaseapp.com",
          "databaseURL": "https://bhprecignition.firebaseio.com",
          "storageBucket": "RichardDavis.appspot.com"
        }
firebase1 = pyrebase.initialize_app(LukeH)  # initialize the communication with the "firebase" servers using the previous config data.
firebase2 = pyrebase.initialize_app(PaulR)
firebase3 = pyrebase.initialize_app(ThomasR)
firebase4 = pyrebase.initialize_app(LukeG)
firebase5 = pyrebase.initialize_app(AlexP)
firebase6 = pyrebase.initialize_app(CaralynH)
firebase7 = pyrebase.initialize_app(RichardD)

while True:
    database = firebase1.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
    gardenMonitoring = database.child("LukeHaeusler")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    luke = gardenMonitoring.child("PersonalPercentage").get().val()

    database = firebase2.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
    gardenMonitoring = database.child("PaulRoff")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    paul = gardenMonitoring.child("PersonalPercentage").get().val()

    database = firebase3.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
    gardenMonitoring = database.child("ThomasRoff")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    thomas = gardenMonitoring.child("PersonalPercentage").get().val()

    database = firebase4.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
    gardenMonitoring = database.child("LukeGrant")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    lukeg = gardenMonitoring.child("PersonalPercentage").get().val()

    database = firebase5.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
    gardenMonitoring = database.child("AlexPerez")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    alex = gardenMonitoring.child("PersonalPercentage").get().val()

    database = firebase6.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
    gardenMonitoring = database.child("CaralynHauser")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    caralyn = gardenMonitoring.child("PersonalPercentage").get().val()

    database = firebase7.database()  # take an instance from the firebase database which is pointing to the root directory of your database.
    gardenMonitoring = database.child("RichardDavis")  # get the child "RGBControl" path in your database and store it inside the "RGBControlBucket" variable.
    richard = gardenMonitoring.child("PersonalPercentage").get().val()

    teamtotal = int(luke) + int(lukeg) + int(caralyn) + int(richard) + int(alex) +int(paul) + int(thomas)
    #teamtotal = int luke + int lukeg + int caralyn + int richard + int alex + int paul + int thomas
    teamtotal = teamtotal /7
    database = firebase1.database()
    gardenMonitoring.child("LukeHaeusler").child("TeamPercentage").set(teamtotal)

    database = firebase1.database()
    gardenMonitoring.child("PaulRoff").child("TeamPercentage").set(teamtotal)

    database = firebase1.database()
    gardenMonitoring.child("ThomasRoff").child("TeamPercentage").set(teamtotal)

    database = firebase1.database()
    gardenMonitoring.child("LukeGrant").child("TeamPercentage").set(teamtotal)

    database = firebase1.database()
    gardenMonitoring.child("AlexPerez").child("TeamPercentage").set(teamtotal)

    database = firebase1.database()
    gardenMonitoring.child("RichardDavis").child("TeamPercentage").set(teamtotal)

    database = firebase1.database()
    gardenMonitoring.child("CaralynHauser").child("TeamPercentage").set(teamtotal)

    atabase = firebase1.database()
    gardenMonitoring.child("OverView").child("TeamPercentage").set(teamtotal)
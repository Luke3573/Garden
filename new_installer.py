# Installer files for new starts.

import time
from subprocess import call
time.sleep(2)
call(sudo apt-get update && sudo apt-get upgrade -y, shell=True)
time.sleep(2)
call(sudo apt install -y build-essential -y, shell=True)
time.sleep(2)
call(sudo apt install python3 -y, shell=True)
time.sleep(2)
call(sudo apt install python3 pip -y, shell=True)
time.sleep(2)
call(sudo apt install remoteit -y, shell=True)
time.sleep(2)
call(sudo apt install connectd -y, shell=True)
time.sleep(2)
call(sudo pip3 install pyserial -y, shell=True)
time.sleep(2)
call(sudo pip3 Adafruit_DHT -y, shell=True)
time.sleep(2)
call(sudo apt install python3 GPIO -y, shell=True)
time.sleep(2)
call(pip3 install piicodev, shell=True)
time.sleep(2)
call(git clone git@github.com:Luke3573/Garden.git, shell=True)

time.sleep(2)
call(sudo apt install git -y, shell=True)
time.sleep(2)
call(pip3 install piicodev, shell=True)





//ESP32 Firebase
#include <WiFi.h>
#include <Firebase.h>
#include <Wire.h>
#include <Adafruit_TMP117.h>
#include <Adafruit_Sensor.h>

// Wi-Fi credentials
#define WIFI_SSID "Luke3573"
#define WIFI_PASSWORD "20062578"

// Firebase Credentials
#define REFERENCE_URL "https://home-garden-25b17.firebaseio.com/"
#define AUTH_TOKEN "AIzaSyB_2lt7J9iazmvtS8Wxw_GTH_Qo37HAT3c"

/* Use the following instance for Test Mode (No Authentication) */
Firebase fb(REFERENCE_URL);

Adafruit_TMP117  tmp117;

unsigned long dataMillis = 0;
int count = 0;

//INPUTS
int onSwitch = 27;
int offSwitch = 4;
int mainValve = 25;
int coValve = 26;
int tankLevel = 34;

int valveStatus;
int Valvestatus;
int valveStatus2;
int valveSystem;
int level;
int on;
int off;

void setup() {
  Serial.begin(115200);
  //PINS

  pinMode(onSwitch, INPUT);
  pinMode(offSwitch, INPUT);
  pinMode(tankLevel, INPUT);
  pinMode(mainValve, OUTPUT);
  pinMode(coValve, OUTPUT);
  //WIFI

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(300);
  }

  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());

  // Try to initialize!
  Serial.println("Adafruit TMP117 Initalized");
  tmp117.begin();
  Serial.println("TMP117 Found!");

}

void loop() {
  if (millis() - dataMillis > 5000) {
    dataMillis = millis();

    //************************INPUTS**********************
    //Read TMP117 temp sensor
    sensors_event_t temp;
    if (!tmp117.begin()) {
      Serial.println("Failed to find TMP117 chip");
    }
      else {
        tmp117.getEvent(&temp); //fill the empty event object with the current measurements
      }
    
    // Read pin INPUTS
    level = analogRead(tankLevel);
    on = digitalRead(onSwitch);
    off = digitalRead(offSwitch);
    
    
    //Caculate tank level
    level = map(level, 87, 188, 0, 100);

    //Update Firebase readings
    fb.setFloat("GMS/temperature", temp.temperature);
    fb.setFloat("GMS/systemActive", valveStatus);
    fb.setFloat("GMS/tankLevel", level);

    //Read System activation status
    Valvestatus = fb.getInt("GMS/valveStatus", valveStatus);
    fb.getInt("GMS/fans", valveStatus2);
    if (valveStatus2 >= 1){
      valveStatus = valveStatus2;
      valveSystem = valveStatus2;
    }

    if (on >= 1){
      fb.setInt("GMS/valveStatus", 1);

    }
    if (off >= 1){
      fb.setInt("GMS/valveStatus", 0);
      fb.setInt("GMS/fans", 0);

    }

    //System Valve Timer
    if (valveStatus >= 1){
      count ++;
      fb.setInt("GMS/humidity", count);
    }
    if (valveStatus <= 0){
      count = 0;
      fb.setInt("GMS/humidity", count);
      fb.setInt("GMS/fans", 0);
    }
    if (count >= 30){
      fb.setInt("GMS/valveStatus", 0);
      fb.setInt("GMS/fans", 0);
    }




   
    



/* - ******************************firebase examples**********************8

    fb.setFloat("GMS/humidity", count++);
    Serial.println(count);


    int temp;
    temps = fb.getInt("GMS/maxtemp", temp);
    Serial.print("Get Int - Response Code: ");
    Serial.println(temps);
    Serial.print("Retrieved Int: ");
    Serial.println(temp);
*/
  }
}

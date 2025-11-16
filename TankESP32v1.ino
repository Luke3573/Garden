//ESP32 Firebase
#include <WiFi.h>
#include <Firebase.h>
#include <Wire.h>
#include <MCP3008.h>

// Wi-Fi credentials
//#define WIFI_SSID "Luke3573"
//#define WIFI_PASSWORD "20062578"
#define WIFI_SSID "Garden"
#define WIFI_PASSWORD "6354207C7A"

// Firebase Credentials
#define REFERENCE_URL "https://home-garden-25b17.firebaseio.com/"
#define AUTH_TOKEN "AIzaSyB_2lt7J9iazmvtS8Wxw_GTH_Qo37HAT3c"

// MCP3008 configuration
#define CS_PIN 5
#define CLOCK_PIN 18
#define MOSI_PIN 23
#define MISO_PIN 19

// Tank sensor input pin
const int tankSensorPin = 34;

/* Use the following instance for Test Mode (No Authentication) */
Firebase fb(REFERENCE_URL);
MCP3008 adc(CLOCK_PIN, MOSI_PIN, MISO_PIN, CS_PIN);


unsigned long dataMillis = 0;
int count = 0;
int count2 = 0;



void setup() {
  Serial.begin(115200);
  
  // Initialize sensor pin as input
  pinMode(tankSensorPin, INPUT);
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
}

void loop() {
  if (millis() - dataMillis > 5000) {
    dataMillis = millis();
    int rawReading = adc.readADC(0);

    float tankLevel = map(rawReading, 87, 188, 0, 100);
    Serial.print("Tank Level: ");
    Serial.println(tankLevel);

    // Send Firebase Data
    fb.setFloat("GMS/tankLevel", tankLevel);

    // system reboot every 4 hours
    count2 ++;
    if (count2 >= 4000){
      ESP.restart();
    }
    Serial.println(count2);
    Serial.println(count);
    
  }
}

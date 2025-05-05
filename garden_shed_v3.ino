/*
  ---------------------------------
  IMPORTANT: Configuration Reminder
  ---------------------------------
  
  Before running this code, make sure to check the "secrets.h" file
  for important configuration details such as Wi-Fi credentials and 
  Firebase settings.

  The "secrets.h" file should include:
  - Your Wi-Fi SSID and Password
  - Your Firebase Realtime Database URL
  - (OPTIONAL) Firebase Authentication Token

  Ensure that "secrets.h" is properly configured and includes the correct
  information for your project. Failure to do so may result in connection
  errors or incorrect behavior of your application.

  Note: The "secrets.h" file should be located in the same directory as
  this sketch.
*/

#include "secrets.h"
#include <Firebase.h>
#include <MCP3008.h>

//Configuration.SetPinFunction(23, DeviceFunction.SPI1_MOSI);
//Configuration.SetPinFunction(19, DeviceFunction.SPI1_MISO);
//Configuration.SetPinFunction(18, DeviceFunction.SPI1_CLOCK);

int tank1 = 34;
float level;
float levels;

#define CS_PIN 5
#define CLOCK_PIN 18
#define MOSI_PIN 23
#define MISO_PIN 19

// put pins inside MCP3008 constructor
MCP3008 adc(CLOCK_PIN, MOSI_PIN, MISO_PIN, CS_PIN);

/* Use the following instance for Test Mode (No Authentication) */
Firebase fb(REFERENCE_URL);

/* Use the following instance for Locked Mode (With Authentication) */
// Firebase fb(REFERENCE_URL, AUTH_TOKEN);

void setup() {
  Serial.begin(115200);
  #if !defined(ARDUINO_UNOWIFIR4)
    WiFi.mode(WIFI_STA);
  #else
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
  #endif
  pinMode(tank1,INPUT);
  
  
}

void tank() {

  //level = analogRead(tank1);
  level = adc.readADC(0); // read Chanel 0 from MCP3008 ADC
  Serial.println(level);
  level = map(level, 87, 188, 0, 100);
  Serial.println(level);
  //levels = analogRead(tank1);
  levels = adc.readADC(0); // read Chanel 0 from MCP3008 ADC

  WiFi.disconnect();
  delay(1000);
  //pinMode(level,INPUT);
  /* Connect to WiFi */
  Serial.println();
  Serial.println();
  Serial.print("Connecting to: ");
  Serial.println(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  fb.setFloat("GMS/bed_battery", levels);
  fb.setFloat("GMS/tankLevel", level);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print("-");
    delay(500);
  }

  Serial.println();
  Serial.println("WiFi Connected");
  Serial.println();

  #if defined(ARDUINO_UNOWIFIR4)
    digitalWrite(LED_BUILTIN, HIGH);
  #endif

  
}

void loop() {
 
  tank();
  /* ----- */ 

  /*
    Set String, Int, Float, or Bool in Firebase
    
    Parameters:
      - path: The path in Firebase where the data will be stored.
      - data: The value to set, which can be of type String, Int, Float, or Bool.

    Returns:
      - HTTP response code as an integer.
        - 200 indicates success.
        - Other codes indicate failure.
  */
  //fb.setString("Example/myString", "Hello World!");
 // fb.setInt("Example/myInt", 123);
 // fb.setFloat("Example/myFloat", 45.67);
  //fb.setBool("Example/myBool", true);

  /*
    Push String, Int, Float, or Bool in Firebase
    
    Parameters:
      - path: The path in Firebase where the data will be stored.
      - data: The value to push, which can be of type String, Int, Float, or Bool.

    Returns:
      - HTTP response code as an integer.
        - 200 indicates success.
        - Other codes indicate failure.
  */
 // fb.pushString("Push", "Foo-Bar");
//  fb.pushInt("Push", 890);
  fb.setFloat("GMS/bed_battery", levels);
  fb.setFloat("GMS/tankLevel", level);
 // fb.pushBool("Push", false);

  /*
    Get String, Int, Float, or Bool from Firebase
    
    Parameters:
      - path: The path in Firebase from which the data will be retrieved.

    Returns:
      - The value retrieved from Firebase as a String, Int, Float, or Bool.
      - If the HTTP response code is not 200, returns NULL (for String) or 0 (for Int, Float, Bool).
  */
//  String retrievedString = fb.getString("Example/myString");
 // Serial.print("Retrieved String:\t");
 // Serial.println(retrievedString);

//  int retrievedInt = fb.getInt("Example/myInt");
 // Serial.print("Retrieved Int:\t\t");
//  Serial.println(retrievedInt);

//  float retrievedFloat = fb.getFloat("GMS/ControlTemp");
//  Serial.print("Retrieved Float:\t");
 // Serial.println(retrievedFloat);

 // bool retrievedBool = fb.getBool("Example/myBool");
//  Serial.print("Retrieved Bool:\t\t");
////  Serial.println(retrievedBool);

  /*
    Remove Data from Firebase
    
    Parameters:
      - path: The path in Firebase from which the data will be removed.

    Returns:
      - HTTP response code as an integer.
        - 200 indicates success.
        - Other codes indicate failure.
  */
  //fb.remove("GSM/tankLevel");

  tank();
}

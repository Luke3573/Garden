const int res = 4;
const int light = 13;

int voltSense = A0;
int count = 0;
int volt;
int voltStatus;

void setup() {
  // put your setup code here, to run once:
  pinMode(res, OUTPUT);
  pinMode(light, OUTPUT);
  pinMode(voltSense, INPUT);
  Serial.begin(9600);
}

void loop() {
  
  
  volt = voltSense;

  if (volt <= 550) {
    count = 0;
    digitalWrite(res, HIGH);
    digitalWrite(light, LOW);
    voltStatus = 0;
  }
  if (voltStatus == 0){
    count = 0;
    if (volt >= 850){
      digitalWrite(res, LOW);
      voltStatus = 1;

    }
  }
  if (voltStatus == 1){
    count ++;
  }
  if (count >= 14400){
    digitalWrite(res, HIGH);
    digitalWrite(light, LOW);
    delay(1000);
    digitalWrite(res, LOW);
    digitalWrite(light, HIGH);
  }

}


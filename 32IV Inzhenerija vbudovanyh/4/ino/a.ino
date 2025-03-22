int switchPin=12;
int ledPin=5;
int powerPin=4;
int plusPin=3;
int minusPin=2;

int brightness=0;

void setup()
{
  pinMode(switchPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(powerPin, INPUT);
  pinMode(plusPin, INPUT);
  pinMode(minusPin, INPUT);
  Serial.begin(9600);
}

void writeLed() {
  analogWrite(ledPin, brightness);
  Serial.println(brightness);
}

void loop()
{
  int switchState=digitalRead(switchPin);
  if (switchState==1) {
    if (digitalRead(powerPin)==1) {
      Serial.println("Power");
      if (brightness>0)
        brightness=0;
      else 
        brightness=130;
      writeLed();
    }
    else if (digitalRead(plusPin)==1) {
      Serial.println("Plus");
      if (brightness<230) brightness+=25;
      writeLed();
    }
    else if (digitalRead(minusPin)==1) {
      Serial.println("Minus");
      if (brightness>25) brightness-=25;
      writeLed();
    }
  }
  delay(100);
}
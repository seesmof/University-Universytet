int sensorPin=3;
int ledPin=13;
bool ledOn=false;
int lastState=0;

void setup()
{
  pinMode(sensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  int sensorPosition=digitalRead(sensorPin);
  if (sensorPosition==HIGH && sensorPosition!=lastState) {
    ledOn=!ledOn;
    digitalWrite(ledPin, ledOn);
  }
  lastState=sensorPosition;
  delay(100);
}
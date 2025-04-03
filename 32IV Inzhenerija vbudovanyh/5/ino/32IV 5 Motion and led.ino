int sensorPin=3;
int ledPin=13;
bool ledOn=false;
bool cycleEnded=false;

void setup()
{
  pinMode(sensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int sensorPosition=digitalRead(sensorPin);
  if (sensorPosition==HIGH) {
    if (!cycleEnded) {
      if (ledOn) digitalWrite(ledPin, HIGH);
      else digitalWrite(ledPin, LOW);
    }
    cycleEnded=false;
  } else {
    cycleEnded=true;
    ledOn=!ledOn;
  }
  Serial.println(cycleEnded);
  Serial.println(ledOn);
  Serial.println("");
  delay(100);
}
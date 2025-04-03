bool ledOn=false;
int sensorPin=3;
int ledPin=13;

void setup()
{
  pinMode(sensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int sensorPosition=digitalRead(sensorPin);
  if (sensorPosition==HIGH){
    ledOn=!ledOn;
  }
  if (ledOn) digitalWrite(ledPin, HIGH);
  else digitalWrite(ledPin, LOW);
  Serial.println(ledOn);
  delay(100);
}
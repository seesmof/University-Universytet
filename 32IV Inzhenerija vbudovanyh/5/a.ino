int sensorPostiion=0;
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
  sensorPostiion=digitalRead(sensorPin);
  if (sensorPostiion==HIGH){
    digitalWrite(ledPin, HIGH);
    Serial.println("Sensor on");
  } else {
    digitalWrite(ledPin, LOW);
  }
  delay(120);
}
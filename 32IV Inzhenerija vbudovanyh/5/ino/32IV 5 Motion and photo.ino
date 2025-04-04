int sensorOn=0;
int sensorPin=3;
int ledPin=13;
int photoPin=A0;
int MIN_PHOTO=6;
int MAX_PHOTO=679;

void setup()
{
  pinMode(sensorPin, INPUT);
  pinMode(photoPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  sensorOn=digitalRead(sensorPin);
  int photoValue=analogRead(photoPin);
  int convertedValue=map(photoValue, MIN_PHOTO, MAX_PHOTO, 1, 100);
  Serial.println(convertedValue);
  if (sensorOn==HIGH && convertedValue>=50){
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
  delay(120);
}
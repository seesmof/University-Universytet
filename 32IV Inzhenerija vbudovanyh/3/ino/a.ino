int MIN_VALUE=85;
int MAX_VALUE=385;

int smokePin=A0;
int ledPin=3;

void setup()
{
  pinMode(ledPin, OUTPUT);
  pinMode(smokePin, INPUT);
}

void loop()
{
  int smokeValue=analogRead(smokePin);
  int convertedValue=map(smokeValue, MIN_VALUE, MAX_VALUE, 0, 100);
  if (convertedValue>50){
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
  delay(100);
}
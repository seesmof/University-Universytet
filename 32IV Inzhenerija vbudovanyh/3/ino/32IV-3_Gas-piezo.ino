int MIN_VALUE=85;
int MAX_VALUE=385;

int smokePin=A0;
int ledPin=7;
int piezoPin=3;

void setup()
{
  pinMode(smokePin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(piezoPin, OUTPUT);
}

void loop()
{
  int smokeValue = analogRead(smokePin);
  int convertedValue = map(smokeValue, MIN_VALUE, MAX_VALUE, 1, 100);
  int delayTime=map(convertedValue, 100, 1, 1, 100);
  delayTime=abs(-delayTime*10);
  digitalWrite(ledPin, HIGH);
  digitalWrite(piezoPin, HIGH);
  delay(delayTime);
  digitalWrite(ledPin, LOW);
  digitalWrite(piezoPin, LOW);
  delay(delayTime);
}
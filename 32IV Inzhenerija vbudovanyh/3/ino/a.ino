int MIN_VALUE=85;
int MAX_VALUE=385;

int smokePin=A0;
int redPin=9;
int greenPin=11;
int bluePin=10;

void setup()
{
  pinMode(smokePin, INPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  digitalWrite(redPin, HIGH);
  digitalWrite(greenPin, HIGH);
  digitalWrite(bluePin, HIGH);
}

void loop()
{
  int smokeValue=analogRead(smokePin);
  int convertedValue=map(smokeValue, MIN_VALUE, MAX_VALUE, 0, 100);
  if (convertedValue>30){
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
  delay(100);
}
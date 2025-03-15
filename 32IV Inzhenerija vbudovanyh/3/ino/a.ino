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

void turnLedOff() {
  digitalWrite(redPin, LOW);
  digitalWrite(greenPin, LOW);
  digitalWrite(bluePin, LOW);
}

void loop()
{
  int smokeValue=analogRead(smokePin);
  int convertedValue=map(smokeValue, MIN_VALUE, MAX_VALUE, 0, 100);
  if (convertedValue<25){
    // Зелений
    digitalWrite(redPin, 138);
    digitalWrite(greenPin, 201);
    digitalWrite(bluePin, 38);
  } else if (convertedValue>=25 && convertedValue<50){
    // Жовтий
    digitalWrite(redPin, 255);
    digitalWrite(greenPin, 202);
    digitalWrite(bluePin, 58);
  } else if (convertedValue>=50 && convertedValue<75){
    // Помаранчевий
    digitalWrite(redPin, 255);
    digitalWrite(greenPin, 146);
    digitalWrite(bluePin, 76);
  } else if (convertedValue>=75){
    // Червоний
    digitalWrite(redPin, 255);
    digitalWrite(greenPin, 89);
    digitalWrite(bluePin, 94);
  } else {
    turnLedOff();
  }
  delay(100);
}
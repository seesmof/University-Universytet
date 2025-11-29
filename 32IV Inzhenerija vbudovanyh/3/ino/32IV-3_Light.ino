int redPin=11;
int greenPin=9;
int bluePin=10;

void setup()
{
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  digitalWrite(redPin, HIGH);
  digitalWrite(greenPin, HIGH);
  digitalWrite(bluePin, HIGH);
}

void loop()
{
  analogWrite(redPin,255);
  analogWrite(greenPin,213);
  analogWrite(bluePin,139);
}
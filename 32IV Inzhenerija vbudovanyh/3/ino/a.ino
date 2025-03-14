int redPin=11;
int greenPin=9;
int bluePin=10;

void setup()
{
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(redPin, OUTPUT);
}

void loop()
{
  analogWrite(greenPin,213);
  analogWrite(bluePin,139);
  analogWrite(redPin,255);
}
int redPin=11;
int greenPin=9;
int bluePin=10;

void setup()
{
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop()
{
  digitalWrite(redPin, 255);
  digitalWrite(greenPin, 0);
  digitalWrite(bluePin, 0);
}
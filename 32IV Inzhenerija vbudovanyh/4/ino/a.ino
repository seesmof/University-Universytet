int pin=5;
int brightness=1;

void setup()
{
  pinMode(pin, OUTPUT);
}

void loop()
{
  brightness+=10;
  analogWrite(pin, brightness);
  delay(300);
  digitalWrite(pin, LOW);
  delay(300);
  if (brightness>=255)
    brightness=0;
}
int MIN_VALUE=85;
int MAX_VALUE=385;

int smokePin=A0;

void setup()
{
  pinMode(smokePin, INPUT);

  Serial.begin(9600);
}

void loop()
{
  int smokeValue = analogRead(smokePin);
  int convertedValue = map(smokeValue, MIN_VALUE, MAX_VALUE, 0, 100);
  Serial.println(convertedValue);
  delay(100);
}
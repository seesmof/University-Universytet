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

  Serial.begin(9600);
}

void turnLedOff() {
  digitalWrite(redPin, LOW);
  digitalWrite(greenPin, LOW);
  digitalWrite(bluePin, LOW);
}

void showRgbColor(int redValue, int greenValue, int blueValue) {
  digitalWrite(redPin, redValue);
  digitalWrite(greenPin, greenValue);
  digitalWrite(bluePin, blueValue);
}

void loop()
{
  int smokeValue = analogRead(smokePin);
  int convertedValue = map(smokeValue, MIN_VALUE, MAX_VALUE, 0, 100);
  Serial.println(convertedValue);

  if (convertedValue<25){
    // Зелений
    showRgbColor(0,255,0);
  } else if (convertedValue>=25 && convertedValue<50){
    // Жовтий
    showRgbColor(255,255,0);
  } else if (convertedValue>=50 && convertedValue<75){
    // Блакитний (помаранчевий не показує)
    showRgbColor(0,255,255);
  } else if (convertedValue>=75){
    // Червоний
    showRgbColor(255,0,0);
  } else {
    turnLedOff();
  }
  delay(100);
}
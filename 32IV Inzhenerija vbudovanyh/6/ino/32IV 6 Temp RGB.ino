int greenLed=7;
int redLed=9;
int blueLed=8;
int tempPin=A0;

int blue=18;
int green=49;
int red=50;

int getTempManual() {
  int value=analogRead(tempPin);
  float volts=value*5.0;
  float percents=volts/1024.0;
  float minusOffset=percents-0.5;
  int degrees=minusOffset*100;
  return degrees;
}

void showRgb(int red, int green, int blue) {
  digitalWrite(redLed, red);
  digitalWrite(greenLed, green);
  digitalWrite(blueLed, blue);
}

void setup()
{
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  pinMode(blueLed, OUTPUT);
  pinMode(tempPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int temperature=getTempManual();
  Serial.println(temperature);
  if (temperature<blue) {
    // Blue
    showRgb(0,0,255);
  } else if (temperature>=blue && temperature<=green) {
    // Green
    showRgb(0,255,0);
  } else if (temperature>=red) {
    // Red
    showRgb(255,0,0);
  }
  delay(100);
}
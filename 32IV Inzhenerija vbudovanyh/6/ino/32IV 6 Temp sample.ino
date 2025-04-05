int greenLed=13;
int yellowLed=11;
int orangeLed=7;
int tempPin=A0;

int firstLevel=20;
int secondLevel=40;
int thirdLevel=70;

int getTempMap() {
  int value=analogRead(tempPin);
  int degreesCelcius=map(((value-20)*3.04), 0, 1023, -40, 125);
  return degreesCelcius;
}

int getTempManual() {
  int value=analogRead(tempPin);
  float volts=value*5.0;
  float percents=volts/1024.0;
  float minusOffset=percents-0.5;
  int degrees=minusOffset*100;
  return degrees;
}

void setup()
{
  pinMode(greenLed, OUTPUT);
  pinMode(yellowLed, OUTPUT);
  pinMode(orangeLed, OUTPUT);
  pinMode(tempPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int temperature=getTempManual();
  Serial.println(temperature);
  if (temperature>=firstLevel || temperature<=firstLevel) {
    digitalWrite(greenLed, HIGH);
  } else {
    digitalWrite(greenLed, LOW);
  }
  if (temperature>=secondLevel) {
    digitalWrite(yellowLed, HIGH);
  } else {
    digitalWrite(yellowLed, LOW);
  }
  if (temperature>=thirdLevel) {
    digitalWrite(orangeLed, HIGH);
  } else {
    digitalWrite(orangeLed, LOW);
  }
  delay(100);
}
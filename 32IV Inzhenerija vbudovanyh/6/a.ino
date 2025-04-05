int greenLed=13;
int yellowLed=11;
int orangeLed=7;
int tempPin=A0;

int getTemperatureInDegrees() {
  int value=analogRead(tempPin);
  int percents=(double) value/1024;
  Serial.println(percents);
  int voltage=percents*5;
  int minusOffset=voltage-0.5;
  int degreesCelcius=minusOffset*100;
  return degreesCelcius;
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
  int temperature=getTemperatureInDegrees();
  delay(100);
}
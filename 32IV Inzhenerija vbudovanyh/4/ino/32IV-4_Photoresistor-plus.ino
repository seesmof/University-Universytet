#include <Servo.h>

int servoPin=3;
int photoPin=A0;

int minValue=6;
int maxValue=679;

Servo servo;

void setup()
{
  servo.attach(servoPin);
  Serial.begin(9600);
}

void loop()
{
  int photoValue=analogRead(photoPin);
  int convertedValue=map(photoValue, minValue, maxValue, 1, 3);
  Serial.println(convertedValue);
  int angle=0;
  if (convertedValue==1) angle=0;
  else if (convertedValue==2) angle=90;
  else if (convertedValue==3) angle=180;
  servo.write(angle);
  delay(100);
}
#include <Servo.h>
Servo servo;

const int sensorPin = 12;
const int servoPin = 7;

long getDistance()
{
  pinMode(sensorPin, OUTPUT);
  digitalWrite(sensorPin, LOW);
  delayMicroseconds(2);
  digitalWrite(sensorPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sensorPin, LOW);

  pinMode(sensorPin, INPUT);
  long dur = pulseIn(sensorPin, HIGH);
  long cm = dur / 29 / 2;
  return cm;
}

void setup()
{
  pinMode(servoPin, OUTPUT);
  servo.attach(servoPin);
}

void loop()
{
  long distance = getDistance();
  int degrees = 90;
  if (distance < 100)
  {
    degrees = 0;
  }
  else if (distance >= 100 && distance <= 300)
  {
    degrees = 180;
  }
  else
  {
    degrees = 90;
  }
  servo.write(degrees);
  delay(1000);
}
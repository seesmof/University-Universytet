#include <Servo.h>
Servo servo;

int switchState = 0;

const int servoPin = 12;
const int switchPin = 11;

void setup()
{
  Serial.begin(9600);
  servo.attach(servoPin);
  pinMode(switchPin, INPUT);
}

void loop()
{
  switchState = digitalRead(switchPin);
  if (switchState == HIGH)
  {
    servo.write(90);
  }
  else
  {
    servo.write(-90);
  }
  delay(12);
}
#include <Servo.h>
Servo servo;

bool on = false;

const int servoPin = 12;

void setup()
{
  Serial.begin(9600);
  servo.attach(servoPin);
}

void loop()
{
  if (on)
  {
    servo.write(180);
  }
  else
  {
    servo.write(-180);
    on = false;
  }
  delay(2000);
}
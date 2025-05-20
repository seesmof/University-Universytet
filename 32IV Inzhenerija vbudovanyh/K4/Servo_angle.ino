#include <Servo.h>
Servo servo;

const int servoPin = 12;

void setup()
{
  Serial.begin(9600);
  servo.attach(servoPin);
}

void loop()
{
  Serial.print("Enter angle. ");
  while (Serial.available()==0) {}
  long angle=Serial.parseInt(SKIP_ALL);
  Serial.println(angle);
  servo.write(angle);
  delay(100);
}
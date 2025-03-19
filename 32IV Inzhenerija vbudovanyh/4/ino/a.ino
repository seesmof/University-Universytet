#include <Servo.h>

const int SERVO_PIN=7;
const int RIGHT=87;
const int LEFT=97;
Servo servo;

void setup()
{
  servo.attach(SERVO_PIN);
  Serial.begin(9600);
}

void loop()
{
  delay(300);
}
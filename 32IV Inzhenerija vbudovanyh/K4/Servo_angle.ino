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
  Serial.println("Enter angle: ");
  while (Serial.available()==0) {}
  long number=Serial.parseInt(SKIP_ALL);
  
  String given=Serial.readString();
  given.trim();
  Serial.println(given);
  delay(1000);
}
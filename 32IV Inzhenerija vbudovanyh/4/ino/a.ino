#include <Servo.h>

const int SERVO_PIN=7;
const int LEFT_PHOTORESISTOR_PIN=11;
const int RIGHT_PHOTORESISTOR_PIN=10;

const int ROTATE_RIGHT=87;
const int ROTATE_LEFT=97;
const int MIN_SENSOR=6;
const int MAX_SENSOR=679;

Servo servo;

void setup()
{
  servo.attach(SERVO_PIN);
  Serial.begin(9600);
}

void loop()
{
  int leftValue=analogRead(LEFT_PHOTORESISTOR_PIN);
  int rightValue=analogRead(RIGHT_PHOTORESISTOR_PIN);
  if (leftValue>rightValue)
    servo.write(ROTATE_LEFT);
  else
    servo.write(ROTATE_RIGHT);
  delay(300);
}
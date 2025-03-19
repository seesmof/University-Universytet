#include <Servo.h>

const int SERVO_PIN=7;
const int LEFT_PHOTORESISTOR_PIN=A0;
const int RIGHT_PHOTORESISTOR_PIN=A1;

const int ROTATE_RIGHT=87;
const int ROTATE_LEFT=97;
const int STOP_ROTATION=93;
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
  Serial.println("Left value: ");
  Serial.println(leftValue);
  Serial.println("Right value: ");
  Serial.println(rightValue);
  Serial.println("Servo value: ");
  Serial.println(servo.read());
  if (leftValue>rightValue)
    servo.write(ROTATE_LEFT);
  else if (rightValue>leftValue)
    servo.write(ROTATE_RIGHT);
  else
    servo.write(STOP_ROTATION);
  delay(300);
}
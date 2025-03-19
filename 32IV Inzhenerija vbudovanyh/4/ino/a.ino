#include <Servo.h>

const int SERVO_PIN=7;
Servo servo;
int angle=0;

void setup()
{
  servo.attach(SERVO_PIN);
  Serial.begin(9600);

  servo.write(angle);
}

void loop()
{
  int angle=servo.read();
  for (int i=angle;i<=360*2;i++){
    servo.write(i);
    Serial.println(i);
  }
  delay(1000);
}
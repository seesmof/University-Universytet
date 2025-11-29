#include <Servo.h>
Servo servo;

#define ZERO_BUTTON 7
#define FOURTY_FIVE_BUTTON 6
#define NINETY_BUTTON 5

const int servoPin = 12;

void setup()
{
  Serial.begin(9600);
  servo.attach(servoPin);
  pinMode(ZERO_BUTTON, INPUT);
  pinMode(FOURTY_FIVE_BUTTON, INPUT);
  pinMode(NINETY_BUTTON, INPUT);
}

void loop()
{
  bool zeroClicked=(bool) digitalRead(ZERO_BUTTON);
  bool fourtyFiveClicked=(bool) digitalRead(FOURTY_FIVE_BUTTON);
  bool ninetyClicked=(bool) digitalRead(NINETY_BUTTON);
  
  if (zeroClicked) {
    servo.write(0);
    Serial.println("0");
  }
  if (fourtyFiveClicked) {
    servo.write(45);
    Serial.println("45");
  }
  if (ninetyClicked) {
    servo.write(90);
    Serial.println("90");
  }
  delay(100);
}
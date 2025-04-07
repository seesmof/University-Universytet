#include <LiquidCrystal.h>

LiquidCrystal lcd(13,12,11,10,9,8);
int upPin=7,downPin=6,goPin=5,backPin=4;

void setup()
{
  pinMode(upPin, INPUT);
  pinMode(downPin, INPUT);
  pinMode(goPin, INPUT);
  pinMode(backPin, INPUT);

  lcd.begin(16,2);
  Serial.begin(9600);
}

void loop()
{
  
  delay(100);
  lcd.clear();
}
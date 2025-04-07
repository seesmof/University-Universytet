#include <Adafruit_LiquidCrystal.h>

Adafruit_LiquidCrystal lcd(0);
int tempPin=A5;

int getTempManual() {
  int value=analogRead(tempPin);
  float volts=value*5.0;
  float percents=volts/1024.0;
  float minusOffset=percents-0.5;
  int degrees=minusOffset*100;
  return degrees;
}

void setup()
{
  pinMode(tempPin, INPUT);
  lcd.begin(16, 2);
  lcd.setBacklight(1);

  lcd.print("0 C");
  lcd.setCursor(0,1);
  lcd.print("-");
  Serial.begin(9600);
}

void loop()
{
  int temperature=getTempManual();
  Serial.println(temperature);
  delay(100);
}
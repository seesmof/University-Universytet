#include <Adafruit_LiquidCrystal.h>

Adafruit_LiquidCrystal lcd(0);

void setup()
{
  lcd.begin(16, 2);
  lcd.setBacklight(1);

  lcd.print("Some");
  lcd.setCursor(0,1);
  lcd.print("here");
  delay(500);
}

void loop()
{
  lcd.setCursor(0, 1);
  lcd.print("text");
  lcd.setBacklight(1);
  delay(500);
}
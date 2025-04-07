#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x20,16,2);

void setup()
{
  lcd.init();
  lcd.backlight();

  lcd.print("Grace");
  lcd.setCursor(0,1);
  lcd.print("To you");
  delay(10);
}

void loop()
{
  lcd.setCursor(0,1);
  lcd.print("From GOD our Father");
  delay(10);
}
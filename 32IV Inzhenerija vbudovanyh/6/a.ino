#include <LiquidCrystal.h>

int tempPin=A5;
int rs=12,en=11,d4=5,d5=4,d6=3,d7=2;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

void setup()
{
  pinMode(tempPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int temperature=analogRead(tempPin)*0.004882814;
  temperature=(temperature-0.5)*100;
  Serial.println(temperature);

  lcd.setCursor(0,1);
  lcd.print(temperature);
  lcd.print(" C");
  delay(100);
  lcd.clear();
}
#include <Adafruit_LiquidCrystal.h>

Adafruit_LiquidCrystal lcd(0);
int tempPin=A5;

int getTempMap() {
  int value=analogRead(tempPin);
  int degreesCelcius=map(((value-20)*3.04), 0, 1023, -40, 125);
  return degreesCelcius;
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
  int temperature=getTempMap();
  Serial.println(temperature);
  delay(100);
}
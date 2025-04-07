#include <LiquidCrystal.h>

LiquidCrystal lcd(13,12,11,10,9,8);
int upPin=7,downPin=6,leftPin=5,rightPin=4;

int getTemperature() {
  float temperature=analogRead(tempPin)*0.004882814;
  temperature=(temperature-0.5)*100.0;
  int tmp=round(temperature);
  return tmp;
}

void setup()
{
  lcd.begin(16,2);
  pinMode(tempPin, INPUT);
  pinMode(upPin, INPUT);
  pinMode(downPin, INPUT);
  pinMode(leftPin, INPUT);
  pinMode(rightPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int temperature = getTemperature();
  lcd.setCursor(0,0);
  lcd.print(temperature);
  lcd.print(" C");
  
  delay(100);
  lcd.clear();
}
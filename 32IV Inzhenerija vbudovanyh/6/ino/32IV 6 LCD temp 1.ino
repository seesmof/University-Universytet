#include <LiquidCrystal.h>

int tempPin=A1;
int rs=12,en=11,d4=5,d5=4,d6=3,d7=2;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

void setup()
{
  lcd.begin(16,2);
  pinMode(tempPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  float temperature=analogRead(tempPin)*0.004882814;
  temperature=(temperature-0.5)*100.0;
  int tmp=round(temperature);
  
  lcd.setCursor(0,0);
  lcd.print(tmp);
  lcd.print(" C");
  
  int filled=map(tmp, -40, 125, 1, 16);
  lcd.setCursor(0,1);
  for(int i=0; i<filled; i++){
    lcd.print("-");
  }

  delay(100);
  lcd.clear();
}
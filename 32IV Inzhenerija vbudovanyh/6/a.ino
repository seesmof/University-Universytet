#include <LiquidCrystal.h>

LiquidCrystal lcd(13,12,11,10,9,8);
int upPin=7,downPin=6,goPin=5,backPin=4;
int cursorRow=0;
bool firstMenu=true;

void setup()
{
  pinMode(upPin, INPUT);
  pinMode(downPin, INPUT);
  pinMode(goPin, INPUT);
  pinMode(backPin, INPUT);

  lcd.begin(16,2);
  Serial.begin(9600);
}

void showFirstMenu() {
  lcd.setCursor(2,0);
  lcd.print("Open");
  lcd.setCursor(2,1);
  lcd.print("Close");
}

void showSecondMenu() {
  lcd.setCursor(2,0);
  lcd.print("Door");
  lcd.setCursor(2,1);
  lcd.print("Window");
}

void updateCursor() {
  if (cursorRow==0) {
    lcd.setCursor(0,0);
  } else { 
    lcd.setCursor(0,1);
  }
  lcd.print("- ");
}

void loop()
{
  int upPressed=digitalRead(upPin);
  int downPressed=digitalRead(downPin);
  int goPressed=digitalRead(goPin);
  int backPressed=digitalRead(backPin);

  if (upPressed) {
    if (cursorRow>0) cursorRow-=1;
  }
  if (downPressed) {
    if (cursorRow<1) cursorRow+=1;
  }

  if (goPressed) {
    if (firstMenu) firstMenu=false;
    else Serial.println("Cannot move further");
  }
  if (backPressed) {
    if (!firstMenu) firstMenu=true;
    else Serial.println("Cannot go back");
  }

  if (firstMenu) {
    showFirstMenu();
  } else {
    showSecondMenu();
  }
  updateCursor();

  delay(100);
  lcd.clear();
}
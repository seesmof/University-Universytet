#include <Keypad.h>
#include <Servo.h>

const byte rowsNum=4;
const byte colsNum=4;

char keys[rowsNum][colsNum]={
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'},
};

byte rowPins[rowsNum]={12,11,10,9};
byte colPins[colsNum]={7,6,5,4};

Keypad k=Keypad(makeKeymap(keys),rowPins,colPins,rowsNum,colsNum);
Servo servo;

int servoPin=3;
int ledPin=13;
int piezoPin=A0;
int movementPin=2;

char keysPressed[5];
char lastKey;
bool isLocked=true;

void lock() {
  servo.write(90);
  digitalWrite(ledPin, HIGH);
}

void open() {
  servo.write(0);
  digitalWrite(ledPin, LOW);
}

void clearCache() {
  keysPressed[0]='0';
  keysPressed[1]='0';
  keysPressed[2]='0';
  keysPressed[3]='0';
  keysPressed[4]='0';
}

void setup()
{
  Serial.begin(9600);
  servo.attach(servoPin);
  lock();
  isLocked=true;
}

void loop()
{
  char key=k.getKey();
  if (key!=NO_KEY) {
    Serial.print("Pressed ");
    Serial.print(key);
    Serial.print(", previous: ");
    Serial.println(lastKey);
    
    if (key=='1') {
      clearCache();
      keysPressed[0]=key;
    } else if (key=='2' && lastKey=='1') {
      keysPressed[1]=key;
    } else if (key=='3' && lastKey=='2' && keysPressed[0]=='1') {
      keysPressed[2]=key;
    } else if (key=='4' && lastKey=='3' && keysPressed[0]=='1' && keysPressed[1]=='2') {
      keysPressed[3]=='4';
    } else if (key=='D' && lastKey=='4' && keysPressed[0]=='1' && keysPressed[1]=='2' && keysPressed[2]=='3') {
      Serial.println("Opened");
      open();
      clearCache();
      isLocked=false;
    } else if (key=='C') {
      clearCache();
      lock();
      isLocked=true;
      Serial.println("Locked");
    } else if (key=='D' && !(lastKey=='4' && keysPressed[0]=='1' && keysPressed[1]=='2' && keysPressed[2]=='3')) {
      clearCache();
      Serial.println("Wrong password");
    } else {
      clearCache();
    }
    lastKey=key;
  }
  
  int movement=digitalRead(movementPin);
  if (movement==HIGH && isLocked==true) {
    Serial.println("Movement when locked");
    tone(piezoPin, 1000, 1000);
  } else {
    digitalWrite(piezoPin, LOW);
  }
  delay(30);
}
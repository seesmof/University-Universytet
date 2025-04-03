#include <Keypad.h>

const byte rowsNum=4;
const byte colsNum=4;

char keys[rowsNum][colsNum]={
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'},
}

byte rowPins[rowsNum]={12,11,10,9};
byte colPins[colsNum]={7,6,5,4};

Keypad k=Keypad(makeKeymap(keys),rowPins,colPins,rowsNum,colsNum);

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  char key=k.getKey();
  if (key!=NO_KEY) {
    Serial.println(key);
  }
}
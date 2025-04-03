#include <Keypad.h>

int rowsNum=4;
int colsNum=4;

char keys[rowsNum][colsNum]={
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'},
}

int rowPins[rowsNum]={12,11,10,9};
int colPins[colsNum]={7,6,5,4};

Keypad k=
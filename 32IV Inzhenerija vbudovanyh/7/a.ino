int A=12;
int B=11;
int C=10;
int D=9;
int E=8;
int F=7;
int G=6;

int leftPin=4;
int rightPin=3;

int counter=0;

bool getMotion(int pin){
  bool help=(bool) digitalRead(pin);
  return help;
}

const int DIGITS_NUMBER=7;
int digits[DIGITS_NUMBER]={A,B,C,D,E,F,G};

int zeroDigits[DIGITS_NUMBER]={1,1,1,1,1,1,0};
int oneDigits[DIGITS_NUMBER]={0,1,1,0,0,0,0};
int twoDigits[DIGITS_NUMBER]={1,1,0,1,1,0,1};
int threeDigits[DIGITS_NUMBER]={1,1,1,1,0,0,1};
int fourDigits[DIGITS_NUMBER]={0,1,1,0,0,1,1};
int fiveDigits[DIGITS_NUMBER]={1,0,1,1,0,1,1};
int sixDigits[DIGITS_NUMBER]={1,0,1,1,1,1,1};
int sevenDigits[DIGITS_NUMBER]={1,1,1,0,0,0,0};
int eightDigits[DIGITS_NUMBER]={1,1,1,1,1,1,1};
int nineDigits[DIGITS_NUMBER]={1,1,1,1,0,1,1};

void setup()
{
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(G, OUTPUT);
}

void zero(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=zeroDigits[i];
    digitalWrite(digit, value);
  }
}

void one(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=oneDigits[i];
    digitalWrite(digit, value);
  }
}

void two(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=twoDigits[i];
    digitalWrite(digit, value);
  }
}

void three(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=threeDigits[i];
    digitalWrite(digit, value);
  }
}

void four(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=fourDigits[i];
    digitalWrite(digit, value);
  }
}

void five(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=fiveDigits[i];
    digitalWrite(digit, value);
  }
}

void six(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=sixDigits[i];
    digitalWrite(digit, value);
  }
}

void seven(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=sevenDigits[i];
    digitalWrite(digit, value);
  }
}

void eight(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=eightDigits[i];
    digitalWrite(digit, value);
  }
}

void nine(){
  for(int i=0; i<DIGITS_NUMBER; i++){
    int digit=digits[i];
    int value=nineDigits[i];
    digitalWrite(digit, value);
  }
}

void chooseNumber(int counterNow) {
  switch (counterNow)
  {
  case 0: zero(); break;
  case 1: one(); break;
  case 2: two(); break;
  case 3: three(); break;
  case 4: four(); break;
  case 5: five(); break;
  case 6: six(); break;
  case 7: seven(); break;
  case 8: eight(); break;
  case 9: nine(); break;
  
  default: break;
  }
}

void loop()
{
  bool left=getMotion(leftPin);
  bool right=getMotion(rightPin);

  if (left) {
    if (counter<9) {
      counter++;
    } else if (counter>=9) {
      counter=0;
    }
    chooseNumber(counter);
  } else if (right) {
    if (counter>0) {
      counter--;
    } else if (counter<=0) {
      counter=9;
    }
    chooseNumber(counter);
  }

  delay(100);
}
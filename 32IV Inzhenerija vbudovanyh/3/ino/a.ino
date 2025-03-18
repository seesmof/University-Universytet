const int RED_PIN=11;
const int GREEN_PIN=9;
const int BLUE_PIN=10;
const int BUTTON_PIN=7;

const int COLORS_ROWS=7;
const int COLORS_COLS=3;
const int COLORS[COLORS_ROWS][COLORS_COLS] = {{255,255,255},{255,0,0},{255,255,0},{0,255,0},{0,255,255},{0,0,255},{255,0,255}};
int row=-1;

void setup()
{
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT);
}

void writeRgb(int redValue, int greenValue, int blueValue){
  digitalWrite(RED_PIN, redValue);
  digitalWrite(GREEN_PIN, greenValue);
  digitalWrite(BLUE_PIN, blueValue);
}

void turnLedOff(){
  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, LOW);
}

void loop()
{
  int buttonState=digitalRead(BUTTON_PIN);
  if (buttonState==1){
    if (row<COLORS_ROWS) row+=1;
    else row=0;
    writeRgb(COLORS[row][0],COLORS[row][1],COLORS[row][2]);
  } else {
    turnLedOff();
  }
  delay(100);
}
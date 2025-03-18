const int RED_PIN=11;
const int GREEN_PIN=9;
const int BLUE_PIN=10;
const int BUTTON_PIN=7;

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

void loop()
{
  
}
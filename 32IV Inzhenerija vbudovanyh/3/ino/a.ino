const int RED_PIN=11;
const int GREEN_PIN=9;
const int BLUE_PIN=10;
const int BUTTON_PIN=7;
const int COLORS[7][3] = [[255,255,255],[255,0,0],[255,255,0],[0,255,0],[0,255,255],[0,0,255],[255,0,255]];

void setup()
{
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT);

  Serial.begin(9600);
}

void writeRgb(int redValue, int greenValue, int blueValue){
  digitalWrite(RED_PIN, redValue);
  digitalWrite(GREEN_PIN, greenValue);
  digitalWrite(BLUE_PIN, blueValue);
}

void loop()
{
  for(int i=0; i<COLORS.length(); i++)
    for (int j=0; j<COLORS[i].length(); j++)
      Serial.println(COLORS[i][j])
}
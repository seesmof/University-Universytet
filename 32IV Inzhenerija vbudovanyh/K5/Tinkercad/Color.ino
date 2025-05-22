#define RED 13
#define GREEN 12
#define BLUE 11
#define RED_BUTTON 8
#define GREEN_BUTTON 4
#define BLUE_BUTTON 2

void setup()
{
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(RED_BUTTON, INPUT);
  pinMode(GREEN_BUTTON, INPUT);
  pinMode(BLUE_BUTTON, INPUT);
  Serial.begin(9600);
  Serial.println("Enter color (Red | Green | Blue).");
}

void writeRgb(int red, int green, int blue) {
  digitalWrite(RED, red);
  digitalWrite(GREEN, green);
  digitalWrite(BLUE, blue);
}

bool getButton(int buttonPin) {
  return (bool) digitalRead(buttonPin);
}

void loop()
{
  String givenColor="";
  if (Serial.available()) {
    givenColor=Serial.readString();
    givenColor.trim();
    givenColor.toLowerCase();
  }

  bool redOn=getButton(RED_BUTTON);
  bool greenOn=getButton(GREEN_BUTTON);
  bool blueOn=getButton(BLUE_BUTTON);
  if (redOn) givenColor="red";
  else if (greenOn) givenColor="green";
  else if (blueOn) givenColor="blue";

  if (givenColor=="red") writeRgb(255,0,0);
  else if (givenColor=="green") writeRgb(0,255,0);
  else if (givenColor=="blue") writeRgb(0,0,255);
  delay(100);
}
int MIN_VALUE=85;
int MAX_VALUE=385;

int smokePin=A0;
int ledPin=7;
int piezoPin=3;

int delayTime=1000;
bool appState=true;

void setup()
{
  pinMode(smokePin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(piezoPin, OUTPUT);

  Serial.begin(9600);
}

void loop()
{
  int smokeValue = analogRead(smokePin);
  int convertedValue = map(smokeValue, MIN_VALUE, MAX_VALUE, 0, 100);
  Serial.println(convertedValue);
  delayTime=convertedValue*10;
  if (appState) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(piezoPin, HIGH);
    appState=false;
  } else {
    digitalWrite(ledPin, LOW);
    digitalWrite(piezoPin, LOW);
    appState=true;
  }
  if (convertedValue<=0 || convertedValue>100){
    delay(1000);
  } else {
    delay(-delayTime);
  }
}
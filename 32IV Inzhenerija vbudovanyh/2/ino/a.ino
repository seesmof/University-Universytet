int cm;
const int distanceThreshold=100;
long readUltrasonicDistance(
  int triggerPin,
  int echoPin
){
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);

  long duration=pulseIn(echoPin, HIGH);
  long cmDistance=duration/29/2;
  return cmDistance;
}

void setup()
{
  Serial.begin(9600);
  pinMode(2, OUTPUT);
}

void loop()
{
  cm=readUltrasonicDistance(7,7);
  Serial.print(cm);
  Serial.print("cm, ");
  if (cm>distanceThreshold){
    digitalWrite(2, LOW);
  } 
  if (cm<=distanceThreshold){
    digitalWrite(2, HIGH);
  }
  delay(100);
}
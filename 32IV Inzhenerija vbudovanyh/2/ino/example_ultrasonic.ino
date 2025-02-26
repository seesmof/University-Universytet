int cm;
const int distanceThreshold = 100;

const int ultrasonicPin = 7;
const int ledPin = 2;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  // without this part the LED is constantly lit
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  pinMode(echoPin, INPUT);
  long duration = pulseIn(echoPin, HIGH);
  long cmDistance = duration / 29 / 2;
  return cmDistance;
}

void setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  cm = readUltrasonicDistance(ultrasonicPin, ultrasonicPin);
  Serial.print(cm);
  Serial.print(" cm\n");
  if (cm > distanceThreshold)
  {
    digitalWrite(ledPin, LOW);
  }
  if (cm <= distanceThreshold)
  {
    digitalWrite(ledPin, HIGH);
  }
  delay(100);
}
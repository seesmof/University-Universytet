const int sensorPin = 12;
const int ledPin = 3;

long getDistance()
{
  pinMode(sensorPin, OUTPUT);
  digitalWrite(sensorPin, LOW);
  delayMicroseconds(2);
  digitalWrite(sensorPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sensorPin, LOW);

  pinMode(sensorPin, INPUT);
  long dur = pulseIn(sensorPin, HIGH);
  long cm = dur / 29 / 2;
  return cm;
}

long convertDistanceRange(long oldValue)
{
  const long oldMin = 0;
  const long oldMax = 300;
  const long newMin = 0;
  const long newMax = 255;

  long oldRange = (oldMax - oldMin);
  long newRange = (newMax - newMin);
  long newValue = (((oldValue - oldMin) * newRange) / oldRange) + newMin;

  return newValue;
}

void setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  long distance = getDistance();
  Serial.print(distance);
  Serial.print(" cm\n");
  delay(500);
  if (distance<0 || distance>300){
    analogWrite(ledPin, LOW);
  } else {
    analogWrite(ledPin, -convertDistanceRange(distance));
  }
}
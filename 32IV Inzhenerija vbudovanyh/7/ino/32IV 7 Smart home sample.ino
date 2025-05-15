int tempPin=A5;
int pirPin=A4;
int photoPin=A3;
int distancePin=A2;
int smokePin=A1;

int getTemperature() {
  int help=analogRead(tempPin);
  float volts=help*5.0;
  float percents=volts/1024.0;
  float minusOffset=percents-0.5;
  int degrees=minusOffset*100;
  return degrees;
}

bool getMotion(){
  bool help=(bool) digitalRead(pirPin);
  return help;
}

int getIllumination(){
  int help=analogRead(photoPin);
  int converted=map(help, 6, 679, 1, 100);
  return converted;
}

long getDistance()
{
  pinMode(distancePin, OUTPUT);
  digitalWrite(distancePin, LOW);
  delayMicroseconds(2);
  digitalWrite(distancePin, HIGH);
  delayMicroseconds(10);
  digitalWrite(distancePin, LOW);

  pinMode(distancePin, INPUT);
  long duration = pulseIn(distancePin, HIGH);
  long cmDistance = duration / 29 / 2;
  return cmDistance;
}

int getSmoke(){
  int help=analogRead(smokePin);
  int converted=map(help, 85, 385, 0, 100);
  return converted;
}

void setup()
{
  pinMode(tempPin, INPUT);
  pinMode(pirPin, INPUT);
  pinMode(photoPin, INPUT);
  pinMode(distancePin, INPUT);
  pinMode(smokePin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int temperature=getTemperature();
  bool isMoving=getMotion();
  int illumination=getIllumination();
  long distance=getDistance();
  int smoke=getSmoke();

  Serial.print("Temperature: ");
  Serial.println(temperature);
  Serial.print("Movement: ");
  Serial.println(isMoving);
  Serial.print("Illumination: ");
  Serial.println(illumination);
  Serial.print("Distance: ");
  Serial.println(distance);
  Serial.print("Smoke: ");
  Serial.println(smoke);
  Serial.println();

  delay(500);
}
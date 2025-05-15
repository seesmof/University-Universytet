int wetGate=50;
const int MIN_SENSOR=0;
const int MAX_SENSOR=876;

void setup()
{
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

void loop()
{
  int wet=analogRead(A0);
  int wetness=map(wet, MIN_SENSOR, MAX_SENSOR, 0, 100);
  Serial.println(wetness);

  if (wetness>wetGate) digitalWrite(13, HIGH);
  else digitalWrite(13, LOW);
  delay(100);
}
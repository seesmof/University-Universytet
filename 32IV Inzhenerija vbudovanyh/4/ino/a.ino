const int MIN_PHOTORESISTOR=6;
const int MAX_PHOTORESISTOR=679;

const int PHOTORESISTOR_PIN=A0;

void setup()
{
  pinMode(PHOTORESISTOR_PIN, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int photoresistorValue=analogRead(PHOTORESISTOR_PIN);
  Serial.println(photoresistorValue);
  delay(100);
}
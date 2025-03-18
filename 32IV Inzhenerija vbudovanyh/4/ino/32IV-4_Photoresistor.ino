const int MIN_PHOTORESISTOR=6;
const int MAX_PHOTORESISTOR=679;

const int PHOTORESISTOR_PIN=A0;
const int LED_PIN=9;

void setup()
{
  pinMode(PHOTORESISTOR_PIN, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int photoresistorValue=analogRead(PHOTORESISTOR_PIN);
  int convertedValue=map(photoresistorValue, MIN_PHOTORESISTOR, MAX_PHOTORESISTOR, 0, 255);
  Serial.println(convertedValue);
  analogWrite(LED_PIN, convertedValue);
  delay(100);
}
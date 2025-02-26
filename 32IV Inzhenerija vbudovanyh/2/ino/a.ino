const int redLedPin = 4;
const int orangeLedPin = 3;
const int yellowLedPin = 2;
const int greenLedPin = 1;
const int blueLedPin = 0;

void loop()
{
  int distance_to_object = 200;
  if (distance_to_object < 50)
  {
    digitalWrite(redLedPin, HIGH);
    digitalWrite(orangeLedPin, HIGH);
    digitalWrite(yellowLedPin, HIGH);
    digitalWrite(greenLedPin, HIGH);
    digitalWrite(blueLedPin, HIGH);
  }
  else if (distance_to_object > 50 && distance_to_object < 100)
  {
    digitalWrite(redLedPin, LOW);
    digitalWrite(orangeLedPin, HIGH);
    digitalWrite(yellowLedPin, HIGH);
    digitalWrite(greenLedPin, HIGH);
    digitalWrite(blueLedPin, HIGH);
  }
  else if (distance_to_object > 100 && distance_to_object < 150)
  {
    digitalWrite(redLedPin, LOW);
    digitalWrite(orangeLedPin, LOW);
    digitalWrite(yellowLedPin, HIGH);
    digitalWrite(greenLedPin, HIGH);
    digitalWrite(blueLedPin, HIGH);
  }
  else if (distance_to_object > 150 && distance_to_object < 200)
  {
    digitalWrite(redLedPin, LOW);
    digitalWrite(orangeLedPin, LOW);
    digitalWrite(yellowLedPin, LOW);
    digitalWrite(greenLedPin, HIGH);
    digitalWrite(blueLedPin, HIGH);
  }
  else if (distance_to_object > 200 && distance_to_object < 300)
  {
    digitalWrite(redLedPin, LOW);
    digitalWrite(orangeLedPin, LOW);
    digitalWrite(yellowLedPin, LOW);
    digitalWrite(greenLedPin, LOW);
    digitalWrite(blueLedPin, HIGH);
  }
  else
  {
    digitalWrite(redLedPin, LOW);
    digitalWrite(orangeLedPin, LOW);
    digitalWrite(yellowLedPin, LOW);
    digitalWrite(greenLedPin, LOW);
    digitalWrite(blueLedPin, LOW);
  }
}
int pin=A0;
int MAX=1023;

void setup()
{
  pinMode(pin, INPUT);
  Serial.begin(9600);
}

int getPotentiometer(){
  int current=analogRead(pin);
  return map(current, 0, MAX, 0, 100);
}

void loop()
{
  int res=getPotentiometer();
  Serial.println(res);
}
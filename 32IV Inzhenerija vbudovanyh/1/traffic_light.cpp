int red=2;
int yellow=1;
int green=0;

void setup(){
  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green,OUTPUT);
}

int delay_time=1000;

void loop(){
  digitalWrite(red,HIGH);
  digitalWrite(yellow,LOW);
  digitalWrite(green,LOW);
  delay(delay_time);

  digitalWrite(red,HIGH);
  digitalWrite(yellow,HIGH);
  digitalWrite(green,LOW);
  delay(delay_time);

  digitalWrite(red,LOW);
  digitalWrite(yellow,LOW);
  digitalWrite(green,HIGH);
  delay(delay_time);
}
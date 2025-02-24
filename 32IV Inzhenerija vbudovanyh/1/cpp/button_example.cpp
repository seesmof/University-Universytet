void setup(){
  pinMode(13,OUTPUT);
  pinMode(10,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  int buttonState=digitalRead(10);
  Serial.println(buttonState);
  if (buttonState==1){
    digitalWrite(13,HIGH);
  } else { digitalWrite(13,LOW); }
}
void setup(){
  for (int i=0; i<6; i++)
    pinMode(i+2,OUTPUT);
}

void loop(){
  for (int i=0; i<6; i++){
    digitalWrite(i+2, HIGH);
    delay(300);
    digitalWrite(i+2, LOW);
    delay(300);
  }
  for (int i=4; i>0; i--){
    digitalWrite(i+2, HIGH);
    delay(300);
    digitalWrite(i+2, LOW);
    delay(300);
  }
}
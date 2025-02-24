int cars_red=2;
int cars_yellow=1;
int cars_green=0;

int pedestrians_red=8;
int pedestrian_green=7;

int button=4;

void setup(){
  pinMode(cars_red,OUTPUT);
  pinMode(cars_yellow,OUTPUT);
  pinMode(cars_green,OUTPUT);

  pinMode(pedestrians_red,OUTPUT);
  pinMode(pedestrian_green,OUTPUT);
}

int phase_wait_time=3000;
int delay_time=1000;

void cars_red_phase(){
  digitalWrite(cars_red,HIGH);
  digitalWrite(cars_yellow,LOW);
  digitalWrite(cars_green,LOW);
  digitalWrite(pedestrians_red,LOW);
  digitalWrite(pedestrian_green,HIGH);
  delay(phase_wait_time-delay_time);
}

void cars_yellow_phase(){
  digitalWrite(cars_red,HIGH);
  digitalWrite(cars_yellow,HIGH);
  digitalWrite(cars_green,LOW);
  digitalWrite(pedestrians_red,LOW);
  digitalWrite(pedestrian_green,HIGH);
  delay(delay_time);
}

void cars_green_phase(){
  digitalWrite(cars_red,LOW);
  digitalWrite(cars_yellow,LOW);
  digitalWrite(cars_green,HIGH);
  digitalWrite(pedestrians_red,HIGH);
  digitalWrite(pedestrian_green,LOW);
  delay(phase_wait_time);
}

void loop(){
  int is_button_pressed=digitalRead(button);
  cars_red_phase();
  cars_yellow_phase();
  cars_green_phase();
}
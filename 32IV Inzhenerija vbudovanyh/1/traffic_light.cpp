int led_red = 2;
int led_yellow = 1;
int led_green = 0;

void setup(){
  pinMode(led_red, OUTPUT);
  pinMode(led_yellow, OUTPUT);
  pinMode(led_green, OUTPUT);
}

int delay_time=1000;

void loop(){
  digitalWrite(led_red, LOW);
  digitalWrite(led_yellow, LOW);
  digitalWrite(led_green, HIGH);
  delay(delay_time);

  digitalWrite(led_red, LOW);
  digitalWrite(led_yellow, HIGH);
  digitalWrite(led_green, LOW);
  delay(delay_time);

  digitalWrite(led_red, HIGH);
  digitalWrite(led_yellow, LOW);
  digitalWrite(led_green, LOW);
  delay(delay_time);
}
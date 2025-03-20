#define DECODE_NEC
#include <IRremote.hpp>

const unsigned int RECEIVER_PIN=3;

const int GREEN_LED_PIN=13;
const int ORANGE_LED_PIN=12;
const int RED_LED_PIN=11;
const int YELLOW_LED_PIN=10;
const int BLUE_LED_PIN=9;
const int WHITE_LED_PIN=8;

void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(RECEIVER_PIN);
  pinMode(GREEN_LED_PIN, OUTPUT);
  pinMode(ORANGE_LED_PIN, OUTPUT);
  pinMode(RED_LED_PIN, OUTPUT);
  pinMode(YELLOW_LED_PIN, OUTPUT);
  pinMode(BLUE_LED_PIN, OUTPUT);
  pinMode(WHITE_LED_PIN, OUTPUT);
}

void turnLedsOff(){
  digitalWrite(GREEN_LED_PIN, LOW);
  digitalWrite(ORANGE_LED_PIN, LOW);
  digitalWrite(RED_LED_PIN, LOW);
  digitalWrite(YELLOW_LED_PIN, LOW);
  digitalWrite(BLUE_LED_PIN, LOW);
  digitalWrite(WHITE_LED_PIN, LOW);
}

void loop()
{
  if (IrReceiver.decode()){
    auto data=IrReceiver.decodedIRData.command;
    Serial.println(data,HEX);
    turnLedsOff();
    // 1
    if (data==0x10){
      digitalWrite(ORANGE_LED_PIN, HIGH);
      digitalWrite(GREEN_LED_PIN, HIGH);
    }
    // 2
    else if (data==0x11){
      digitalWrite(WHITE_LED_PIN, HIGH);
      digitalWrite(RED_LED_PIN, HIGH);
    }
    // 3
    else if (data==0x12){
      digitalWrite(YELLOW_LED_PIN, HIGH);
      digitalWrite(BLUE_LED_PIN, HIGH);
    }
    // 4
    else if (data==0x14){
      digitalWrite(GREEN_LED_PIN, HIGH);
      digitalWrite(WHITE_LED_PIN, HIGH);
    }
    IrReceiver.resume();
  }
  delay(100);
}
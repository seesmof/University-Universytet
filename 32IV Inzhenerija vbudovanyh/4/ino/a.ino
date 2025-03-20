#define DECODE_NEC
#include <IRremote.hpp>

const unsigned int RECEIVER_PIN=5;
const unsigned int SWITCH_PIN=2;
const unsigned int LED_PIN=3;
int brightness=1;
int switchValue=0;
bool ledOff=true;

void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(RECEIVER_PIN);
  pinMode(SWITCH_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void changeLed(){
  int value = map(brightness, 1, 10, 0, 255);
  analogWrite(LED_PIN, value);
  Serial.println(value);
}

void loop()
{
  switchValue=digitalRead(SWITCH_PIN);
  if (IrReceiver.decode() && switchValue==1){
    auto data=IrReceiver.decodedIRData.command;

    // Power
    if (data==0x0){
      if (ledOff==true){
        digitalWrite(LED_PIN, HIGH);
        ledOff=false;
      } else if (ledOff==false){
        changeLed();
        ledOff=true;
      }
    }
    // +
    else if (data==0x1) {
      if (brightness<10) brightness+=1;
      changeLed();
    }
    // -
    else if (data==0x9){
      if (brightness>1) brightness-=1;
      changeLed();
    }

    IrReceiver.resume();
  }
  delay(100);
}
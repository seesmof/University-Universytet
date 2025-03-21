#define DECODE_NEC
#include <IRremote.hpp>

const unsigned int RECEIVER_PIN=5;
const unsigned int SWITCH_PIN=2;
const unsigned int LED_PIN=3;
int brightness=25;
int switchValue=0;

void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(RECEIVER_PIN);
  pinMode(SWITCH_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void changeLed(int brightness){
  analogWrite(LED_PIN, brightness);
  Serial.println(brightness);
}

void loop()
{
  switchValue=digitalRead(SWITCH_PIN);
  if (IrReceiver.decode() && switchValue==1){
    auto data=IrReceiver.decodedIRData.command;

    // Power
    if (data==0x0){
      if (brightness>1) brightness=0;
      else brightness=255;
      changeLed();
    }
    // +
    else if (data==0x1) {
      if (brightness<230) brightness+=25;
      changeLed();
    }
    // -
    else if (data==0x9){
      if (brightness>25) brightness-=25;
      changeLed();
    }
    
    IrReceiver.resume();
  }
  delay(300);
}
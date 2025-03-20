#define DECODE_NEC
#include <IRremote.hpp>

const unsigned int RECEIVER_PIN=5;
const unsigned int SWITCH_PIN=2;
const unsigned int LED_PIN=3;
int brightness=1;
int switchValue=0;

void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(RECEIVER_PIN);
  pinMode(LED_PIN, OUTPUT);
}

void loop()
{
  switchValue=digitalRead(SWITCH_PIN);
  Serial.println(switchValue);

  if (IrReceiver.decode() && switchValue==1){
    auto data=IrReceiver.decodedIRData.command;
    Serial.println(data,HEX);

    // Power
    if (data==0x0){

    }
    // +
    else if (data==0x1) {
      if (brightness<10){
        brightness+=1;

      }
    }
    // -
    else if (data==0x9)

    IrReceiver.resume();
  }
  delay(100);
}
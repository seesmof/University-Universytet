#define DECODE_NEC
#include <IRremote.hpp>

const unsigned int RECEIVER_PIN=3;

void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(RECEIVER_PIN);
}

void loop()
{
  if (IrReceiver.decode()){
    auto data=IrReceiver.decodedIRData.command;
    Serial.println(data,HEX);
    IrReceiver.resume();
  }
  delay(100);
}
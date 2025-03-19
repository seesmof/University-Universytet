#define RECIEVER_PIN 3
#include <IRremote.hpp>

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

uint16_t receiveSignal(){
  uint16_t received = 0;

  if (IrReceiver.decode()){
    if (IrReceiver.decodedIRData.protocol==UNKNOWN){
      IrReceiver.printIRResultRawFormatted(&Serial,true);
    }
    if (IrReceiver.decodedIRData.protocol==NEC){
      received=IrReceiver.decodedIRData.command;
      Serial.println(received,HEX);
    }
    IrReceiver.resume();
  }
  return received;
}

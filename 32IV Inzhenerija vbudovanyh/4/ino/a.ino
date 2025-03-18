#define DECODE_NEC
#include <IRremote.hpp>

const int RECEIVER_PIN=3;
void setup()
{
  Serial.begin(9600);
  IrReceiver.begin(RECEIVER_PIN);
}

void loop()
{
  receiveSignal();
}

uint16_t receiveSignal(){
  uint16_t received{0};

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

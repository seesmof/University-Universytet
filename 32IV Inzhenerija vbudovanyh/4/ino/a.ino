#include <IRremote.hpp>

const int RECEIVER_PIN=3;
IRrecv receiver(RECEIVER_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  receiver.enableIRIn();
}

void loop()
{
  if (receiver.decode(&results)){
    Serial.println(results.value,HEX);
    receiver.resume();
  }
}
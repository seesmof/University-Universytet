#define _DISABLE_TLS_
#include "DHTesp.h"
#include <WiFi.h>

#define USERNAME "username"
#define DEVICE_ID "device_id"
#define DEVICE_CREDENTIAL "device_creds"
#define SSID "Wokwi-GUEST"
#define SSID_PASSWORD ""

DHTesp dht;
#define DHT_PIN 15

void setup() {
  Serial.begin(115200);
  
  dht.setup(DHT_PIN, DHTesp::DHT22);
}

void loop() {
  TempAndHumidity data = dht.getTempAndHumidity();
  Serial.println("Temp: "+String(data.temperature,2)+"C");
  Serial.println("Humidity: "+String(data.humidity,1)+"%");
  Serial.println("---");
  delay(1000);
}

void InitWiFi() {
  Serial.println("Connecting to WiFi ...");
  WiFi.begin(SSID, SSID_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);Serial.print(".");
  }
  Serial.println("Connected to WiFi");
}
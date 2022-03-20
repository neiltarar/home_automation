//Libraries
#include <DHT.h>

//Constants
#define DHTPIN 7   // DHT data pin connected to pin 7 on Arduino Board
#define DHTTYPE DHT22  // DHT 22  (AM2302)
#define RELAYPIN 3 // Relay pin connected to pin 3 on Arduino Board

DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino

//Variables
int chk;
float hum;  //Stores humidity value
float temp; //Stores temperature value

void setup()
{
  Serial.begin(9600);
  pinMode(RELAYPIN, OUTPUT); // Setting pin 3 as an output pin to switch on and off the relay
  dht.begin();
}

void loop()
{
    // send data only when you receive data:
    if (Serial.available() > 0) {
      String data = Serial.readStringUntil('\n');      
      if (data == "read_temp") {
        delay(50);
        temp = dht.readTemperature();
        Serial.println(temp);
//        Serial.println(" Celsius");
      } 
      else if (data == "read_hum") {
        hum = dht.readHumidity();
        delay(50);
//        Serial.print("% ");
        Serial.println(hum);
      }
      else if (data == "led_on") {
        digitalWrite(RELAYPIN, HIGH);
      }
      else if (data == "led_off") {
        digitalWrite(RELAYPIN, LOW);
      }
    }
}
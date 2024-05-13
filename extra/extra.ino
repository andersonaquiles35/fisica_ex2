#include <Ultrasonic.h>
HC_SR04 sensor(3,2);

void setup() {
  Serial.begin(9600);
}

void loop() {
  while(true){
    Serial.println(sensor.distance());
    delay(5);
  }
}

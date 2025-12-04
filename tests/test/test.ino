#include <Servo.h>
Servo yaw;

void setup() {
  Serial.begin(9600);
  yaw.attach(9);
  delay(500);
}

void loop() {
  yaw.write(0);
  delay(1000);
  yaw.write(90);
  delay(1000);
  yaw.write(180);
  delay(1000);
}
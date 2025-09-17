#include <Servo.h>
Servo yaw;
int p_potentiometer = 0;
int potentiometer = 0;
int degree_delay = 5;
int sweep_delay = 100;

void setup() {
  Serial.begin(9600);
  yaw.attach(9);
}

void loop() {
    for (int deg = 0; deg <= 180; deg += 1) {
      yaw.write(deg);
      delay(degree_delay);
      Serial.println(yaw.read());
    } 
    delay(sweep_delay);
    for (int deg = 180; deg >= 0; deg -= 1) {
      yaw.write(deg);
      delay(degree_delay);
      Serial.println(yaw.read());
    }
    delay(sweep_delay);
}

#include <Ultrasonic.h>
#include <Servo.h>

int distance = 0;
int p_sonar = 4;
Ultrasonic sonar(p_sonar);

Servo yaw;
int p_potentiometer = 0;
int potentiometer = 0;
int degree_delay = 5;
int sweep_delay = 100;
int now_mili = 0;
int last_mili = 0;

void setup() {
    Serial.begin(9600, SERIAL_8N2);
    yaw.attach(9);
    char output[1000] = "";
}

void loop() {
    distance = sonar.MeasureInCentimeters();

    for (int deg = 0; deg <= 180; deg += 10) {
      distance = sonar.MeasureInCentimeters();
      yaw.write(deg);
      char output[1000] = "";
      delay(degree_delay);
      sprintf(output, "(%d, %d)", deg, distance);
      Serial.println(output);
      delay(500);
    } 
    delay(sweep_delay);
    for (int deg = 180; deg >= 0; deg -= 10) {
      distance = sonar.MeasureInCentimeters();
      yaw.write(deg);
      char output[1000] = "";
      delay(degree_delay);
      sprintf(output, "(%d, %d)", deg, distance);
      Serial.println(output);
      delay(500);
    }
    delay(sweep_delay);
}
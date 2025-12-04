#include <Ultrasonic.h>
#include <Servo.h>

int distance = 0;
int p_sonar = 4;
Ultrasonic sonar(p_sonar);
Servo yaw;
int degree_delay = 10;

void setup() {
  Serial.begin(115200);
  yaw.attach(9);
  delay(500);
}

void loop() {
  distance = sonar.MeasureInCentimeters();
  char output[1000] = "";

  for (int deg = 0; deg < 180; deg += 1) {
    yaw.write(deg);
    if (millis() % 41 == 0) {
      distance = sonar.MeasureInCentimeters();
      sprintf(output, "(%d, %d)", deg, distance);
      Serial.println(output);
    }
    delay(degree_delay);
  }
  
  for (int deg = 179; deg >= 0; deg -= 1) {
    yaw.write(deg);
    if (millis() % 41 == 0) {
      distance = sonar.MeasureInCentimeters();
      sprintf(output, "(%d, %d)", deg, distance);
      Serial.println(output);
    }
    delay(degree_delay);
  }
}
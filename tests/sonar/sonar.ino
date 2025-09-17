#include <Ultrasonic.h>

int distance = 0;
int p_sonar = 4;
Ultrasonic sonar(p_sonar);

void setup() {
    Serial.begin(9600);
}

void loop() {
    distance = sonar.MeasureInCentimeters();
    if (distance <= 400) {
        Serial.println(distance);
    } else {
        Serial.println("Out of range");
    }
}
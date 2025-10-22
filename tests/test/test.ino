#include <Servo.h>
#include <Ultrasonic.h>
using namespace std;

int p_yaw = 9;
int p_sonar = 4;
int dist = 0;
int yaw = 0;
Servo servo;
Ultrasonic sonar(p_sonar)

void setup() {
  Serial.begin(9600);
  yaw.attach(p_yaw);
}

void loop() {
  yaw = servo.read();
  dist = sonar.MeasureInCentimeters();

  char yawstr[1000];
  char diststr[1000];
  sprintf(yawstr, "%d", yaw);
  sprintf(diststr, "%d", dist);
  Serial.print("(");
  Serial.print(yawstr);
  Serial.print(", ");
  Serial.print(diststr);
  Serial.println(")");
}

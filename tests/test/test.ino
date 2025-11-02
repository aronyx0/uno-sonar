#include <Servo.h>
#include <Ultrasonic.h>
#include <string.h>
using namespace std;

int p_yaw = 9;
int p_sonar = 4;
int p_pot = 0;
int dist = 0;
int yaw = 0;
int pot = 0;
float pi = 3.1415927;
Servo servo;
Ultrasonic sonar(p_sonar);

void setup() {
  Serial.begin(9600);
  servo.attach(p_yaw);
}

void loop() {
  //yaw = servo.read();
  int dist = sonar.MeasureInCentimeters();
  int pot = analogRead(p_pot) * 180 / 1023;

  char output[1000] = "";
  //char yawstr[1000];
  char diststr[1000];
  char potstr[1000];
  //sprintf(yawstr, "%d", yaw);
  sprintf(diststr, "%d", dist);
  sprintf(potstr, "%d", pot);

  strcat(output, "(");
  strcat(output, potstr);
  strcat(output, ", ");
  strcat(output, diststr);
  strcat(output, ")");

  /*
  Serial.print("(");
  //Serial.print(yawstr);
  Serial.print(potstr);
  Serial.print(", ");
  Serial.print(diststr);
  Serial.println(")");
  */

  Serial.println(output);

  delay(30);
}

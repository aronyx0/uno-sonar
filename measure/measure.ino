#include <Ultrasonic.h>
#include <Servo.h>
#include <U8g2lib.h>

Servo yaw;
Ultrasonic sonar(4);
U8G2_SSD1306_128X64_NONAME_F_HW_I2C display(U8G2_R2, SCL, SDA, U8X8_PIN_NONE);

void setup() {
	Serial.begin(115200);
	yaw.attach(9);
	display.begin();
	delay(500);
	yaw.write(90);
}

void loop() {
	int distance = sonar.MeasureInCentimeters();
	display.clearBuffer();
	display.setFont(u8g2_font_spleen16x32_mn);
	display.setCursor(5, 31);
	display.print(distance);
	display.setCursor(64, 31);
	display.print(" cm");
	display.sendBuffer();
	delay(100);
}
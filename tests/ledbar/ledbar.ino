#include <Grove_LED_Bar.h>

Grove_LED_Bar bar(3, 2, 0);
int p_potentiometer = 0;

void setup() {
	Serial.begin(9600);
}

void loop() {
	int bar_level = analogRead(p_potentiometer) * 10 / 735;
	Serial.println(bar_level);
	if (bar_level == 1 && millis()/250 % 2) {
		bar_level = 0;
	} else if (bar_level == 2 && millis()/250 % 2) {
		bar_level = 1;
	}
	bar.setLevel(bar_level);
	delay(250);
}
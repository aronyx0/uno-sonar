#include <U8g2lib.h>
#include <Wire.h>

int p_potentiometer = 0;

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* clock=*/ SCL, /* data=*/ SDA, /* reset=*/ U8X8_PIN_NONE);  // High speed I2C

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  int potentiometer = analogRead(p_potentiometer);
  u8g2.clearBuffer();					// clear the internal memory
  u8g2.setFont(u8g2_font_inr16_mf);	// choose a suitable font
  u8g2.print(potentiometer);	// write something to the internal memory
  u8g2.sendBuffer();					// transfer internal memory to the display
  delay(100);  
}
#include <U8g2lib.h>
#include <Wire.h>

int p_potentiometer = 0;

U8G2_SSD1306_128X64_NONAME_F_HW_I2C display(U8G2_R2, SCL, SDA, U8X8_PIN_NONE);

void setup(void) {
  display.begin();
}

void loop(void) {
  int potentiometer = analogRead(p_potentiometer);
  display.clearBuffer();
  display.setFont(u8g2_font_spleen16x32_mn);
  display.setCursor(5, 31);
  display.print(potentiometer);
  display.setCursor(64, 31);
  display.print("/735");
  display.sendBuffer();
  delay(100);
}
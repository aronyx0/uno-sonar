int p_buzzer = 5;
int p_button = 4;

void setup() {
    Serial.begin(9600);
  
}

void loop() {
    /*
    880@8
    698@8
    880@8
    988@8
    1047@8
    988@8
    880@8
    698@8
    659@2

    2:992 ms
    4:496 ms
    8:248 ms
    */

    if (digitalRead(p_button) == HIGH) {
        tone(p_buzzer, 880);
        delay(248);
        noTone(p_buzzer);
        tone(p_buzzer, 698);
        delay(248);
        noTone(p_buzzer);
        tone(p_buzzer, 880);
        delay(248);
        noTone(p_buzzer);
        tone(p_buzzer, 988);
        delay(248);
        noTone(p_buzzer);
        tone(p_buzzer, 1047);
        delay(248);
        noTone(p_buzzer);
        tone(p_buzzer, 988);
        delay(248);
        noTone(p_buzzer);
        tone(p_buzzer, 880);
        delay(248);
        noTone(p_buzzer);
        tone(p_buzzer, 698);
        delay(248);
        noTone(p_buzzer);
        tone(p_buzzer, 659);
        delay(992);
        noTone(p_buzzer);
    }
}

#include <NewRemoteTransmitter.h>

// Transmitter address 0, pin 2, 260ms duration, retransmit 2^3 = 8 times
NewRemoteTransmitter transmitter(0, 2, 260, 1);

void setup() {
}

void turn_on() {
  // Turn unit 0 on
  transmitter.sendUnit(0, true);
}

void turn_off() {
  // Turn unit 0 on
  transmitter.sendUnit(0, false);
}

void dot() {
turn_on();
delay(500);
turn_off();
delay(500);
}

void dash() {
turn_on();
delay(1500);
turn_off();
delay(500);
}

void loop() {

// L
// .
dot();
// -
dash();
// .
dot();
// .
dot();

// end letter
delay(1000);

// S
// .
dot();
// .
dot();
// .
dot();

// end letter
delay(1000);

// D
// -
dash();
// .
dot();
// .
dot();

// end letter
delay(1000);

// end word
delay(2000);

// P
// .
dot();
// -
dash();
// -
dash();
// .
dot();

// end letter
delay(1000);

// I
// .
dot();
// .
dot();

// end letter
delay(1000);

// C
// -
dash();
// .
dot();
// -
dash();
// .
dot();

// end letter
delay(1000);

// K
// -
dash();
// .
dot();
// -
dash();

// end letter
delay(1000);

// N
// -
dash();
// .
dot();

// end letter
delay(1000);

// I
// .
dot();
// .
dot();

// end letter
delay(1000);

// C
// -
dash();
// .
dot();
// -
dash();
// .
dot();

// end letter
delay(1000);

// K
// -
dash();
// .
dot();
// -
dash();

// end letter
delay(1000);

// end word
delay(2000);

// M
// -
dash();
// -
dash();

// end letter
delay(1000);

// O
// -
dash();
dash();
// -
dash();

// end letter
delay(1000);

// R
// .
dot();
// -
dash();
// .
dot();

// end letter
delay(1000);

// G
// -
dash();
// -
dash();
// .
dot();

// end letter
delay(1000);

// E
// .
dot();

// end letter
delay(1000);

// N
// -
dash();
// .
dot();

// end letter
delay(1000);

// repeat message
delay(5500);
}

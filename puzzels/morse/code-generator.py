#! /usr/bin/env python

MORSE_TICK = 500
MESSAGE = "LSD PICKNICK MORGEN"

DOT_TICKS = 1 * MORSE_TICK
DASH_TICKS = 3 * MORSE_TICK
SYMBOL_PAUSE = 1 * MORSE_TICK
LETTER_PAUSE = 3 * MORSE_TICK
WORD_PAUSE = 7 * MORSE_TICK
MESSAGE_PAUSE = 14 * MORSE_TICK

MORSE_DICT = { 'A':'.-', 'B':'-...', 
				'C':'-.-.', 'D':'-..', 'E':'.', 
				'F':'..-.', 'G':'--.', 'H':'....', 
				'I':'..', 'J':'.---', 'K':'-.-', 
				'L':'.-..', 'M':'--', 'N':'-.', 
				'O':'---', 'P':'.--.', 'Q':'--.-', 
				'R':'.-.', 'S':'...', 'T':'-', 
				'U':'..-', 'V':'...-', 'W':'.--', 
				'X':'-..-', 'Y':'-.--', 'Z':'--..', 
				'1':'.----', '2':'..---', '3':'...--', 
				'4':'....-', '5':'.....', '6':'-....', 
				'7':'--...', '8':'---..', '9':'----.', 
				'0':'-----', ', ':'--..--', '.':'.-.-.-', 
				'?':'..--..', '/':'-..-.', '-':'-....-', 
				'(':'-.--.', ')':'-.--.-'}

def delay(length):
	print("delay(" + str(length) + ");")

def turn_on():
	print("turn_on();")

def turn_off():
	print("turn_off();")

def comment(text):
	print("// " + text)

def newline():
	print()

def functions():
	print()

def dot():
	comment('.')
	print("dot();")

def dash():
	comment('-')
	print("dash();")

if __name__ == "__main__":
	print("void dot() {")
	turn_on()
	delay(DOT_TICKS)
	turn_off()
	delay(SYMBOL_PAUSE)
	print("}")
	newline()
	print("void dash() {")
	turn_on()
	delay(DASH_TICKS)
	turn_off()
	delay(SYMBOL_PAUSE)
	print("}")
	newline()
	print("void loop() {")

	for c in MESSAGE:
		if c == ' ':
			newline()
			comment("end word")
			delay(WORD_PAUSE - LETTER_PAUSE)
		else:
			newline()
			comment(c)
			for m in MORSE_DICT[c]:
				dot() if m == '.' else dash()

			newline()
			comment("end letter")
			delay(LETTER_PAUSE - SYMBOL_PAUSE)

	newline()
	comment("repeat message")
	delay(MESSAGE_PAUSE - (LETTER_PAUSE - SYMBOL_PAUSE) - SYMBOL_PAUSE)

	print("}")
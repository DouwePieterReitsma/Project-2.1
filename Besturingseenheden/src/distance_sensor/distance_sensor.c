/*
 * distance_sensor.c
 *
 * Created: 15-11-2018 12:27:34
 *  Author: dprei
 */ 

#include "distance_sensor.h"

static float oldnumresult;		//needed variables for the leds later on
static float numresult;			//idem
/*---------------------------------Initialize ports, timer, interrupts ----------------------------------------------*/
void init() {
	DDRB = 0xFF;
	DDRC = 0xFF;							// Port C all output.
	DDRC &= ~(1<<DDC5);						// Set Pin C5 as input to read Echo
	PORTC |= (1<<PORTC5);					// Enable pull up on C5
	PORTC &= ~(1<<PC4);						// Init C4 as low (trigger)

	PRR &= ~(1<<PRTIM1);					// To activate timer1 module
	TCNT1 = 0;								// Initial timer value
	TCCR1B |= (1<<CS11);					// Timer with pre scaler on 8 , because the 328p has a 16 mhz frequency . so 2 cpu cycles is one 1us
	TCCR1B |= (1<<ICES1);					// First capture on rising edge

	PCICR = (1<<PCIE1);						// Enable PCINT[14:8] we use pin C5 which is PCINT13
	PCMSK1 = (1<<PCINT13);					// Enable C5 interrupt
	sei();									// Enable Global Interrupts
}

/*-------------------------------------Main code----------------------------------*/
int main() {
	uart_init();								// initialize code for serial connection
	init();
		while (1) {
		_delay_ms(60); 							// To have sufficient time between pulses (60ms min)
		PORTC |= (1<<PC4);						// Set trigger high
		_delay_us(10);							// for 10uS
		PORTC &= ~(1<<PC4);						//end of the pulse and trigger the ultrasonic sensor
		
	}
	
}

void transmit_message(const char* message)		//function for transmitting the message that's put in characters in the buffer
{
	for(;*message != '\0'; message++)
	{
		transmit(*message);
	}
}

/*------------------------Interrupt PCINT1 for PIN C5 -----------------------------------------*/
ISR(PCINT1_vect) {
	if (bit_is_set(PINC,PC5)) {					// Checks if echo is high
		TCNT1 = 0;								// Reset Timer		
	} else {
		uint16_t tnum = TCNT1;					// Save Timer value
		uint8_t oldSREG = SREG;
		char buffer[10];						// creating variable buffer
		
		cli();									// Disable Global interrupts

		oldnumresult = numresult;
		numresult = tnum/58/2;
		sprintf(buffer, "%d",tnum/58/2);
		transmit_message(buffer);				// transmitting the distance in cm

		_delay_ms(1000);						// delay so the distance gets send every second
		SREG = oldSREG;							// Enable interrupts
												// the code beneath this line is for the leds
		if (numresult <= 5){
			PORTB |= _BV(PB2);
			PORTB &= ~_BV(PB3);
			PORTB &= ~_BV(PB1);
		}										//PB1 = yellow, PB2 = red, PB3 = green
		else if (oldnumresult - numresult < -1) {//change the -1 to 0 if you don't need the precaution
			PORTB |= _BV(PB1);					//PinB1 high
			PORTB |= _BV(PB3);					//PinB3 high
			PORTB &= ~_BV(PB2);					//PinB2 low
			_delay_ms(100);
			PORTB &= ~_BV(PB1);					//PinB1 low
			_delay_ms(100);
			PORTB |= _BV(PB1);					//PinB1 High
			_delay_ms(100);
			PORTB &= ~_BV(PB1);
			_delay_ms(100);
			PORTB |= _BV(PB1);
			_/*delay_ms(100);
			PORTB &= ~_BV(PB1);
			_delay_ms(100);
			PORTB |= _BV(PB1);
			_delay_ms(100);				//if you want extra flashes didn't have time to make a function for the flashing
			PORTB &= ~_BV(PB1);
			_delay_ms(100);
			PORTB |= _BV(PB1);*/
			
				
		}
		else if (oldnumresult - numresult > 1) {	
			PORTB &= ~_BV(PB3);				//change the 1 to 0 if you don't need the precaution
			PORTB |= _BV(PB2);
			PORTB |= _BV(PB1);
			_delay_ms(100);
			PORTB &= ~_BV(PB1);
			_delay_ms(100);
			PORTB |= _BV(PB1);
			_delay_ms(100);
			PORTB &= ~_BV(PB1);
			_delay_ms(100);
			PORTB |= _BV(PB1);
			/*_delay_ms(100);
			PORTB &= ~_BV(PB1);
			_delay_ms(100);
			PORTB |= _BV(PB1);
			_delay_ms(100);			//if you want extra flashes
			PORTB &= ~_BV(PB1);
			_delay_ms(100);
			PORTB |= _BV(PB1);*/
			
		}
		else {
			PORTB |= _BV(PB3);
			PORTB &= ~_BV(PB2);
			PORTB &= ~_BV(PB1);
		}
}
}
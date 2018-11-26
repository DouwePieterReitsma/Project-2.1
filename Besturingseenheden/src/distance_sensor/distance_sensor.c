/*
 * distance_sensor.c
 *
 * Created: 15-11-2018 12:27:34
 *  Author: dprei
 */ 

#include "distance_sensor.h"

#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdint.h>

#define F_CPU 16E6

#include <util/delay.h>

#include "../common/analog.h"
#include "../common/serial.h"
#include "../common/sensor_protocol.h"

#define TRIGGER_PIN 3
#define ECHO_PIN 2

uint16_t counter = 0; // counter for timer0

float previous_distance;
float distance;

void init_distance_sensor() 
{
    // port setup
	DDRD &= ~(1 << ECHO_PIN);	// set input port
    DDRD |= (1 << TRIGGER_PIN); // set output port
    
	PORTD &= ~(1 << TRIGGER_PIN); // clear trigger port
    
    // interrupt setup
    PCICR = (1 << PCIE0); // enable PCMSK0 scan
    PCMSK0 |= (1 << PCINT18); // enable external interrupts on PD2
    sei(); // enable global interrupts
}

void measure_distance(void)
{
    counter = 0;
    
    PORTD |= (1 << TRIGGER_PIN); // set trigger high
    _delay_us(10); // trigger 10 us pulse
    PORTD &= ~(1 << TRIGGER_PIN); // set trigger low
}

void transmit_distance(void)
{
    char buffer[50];
    SensorData data;
    int result = 0;
    
    data.type = SENSOR_TYPE_DISTANCE;
    data.data.distance = distance;
    
    result = serialize_sensor_data(&data, buffer);
    
    if(result)
    {
        transmit_message(buffer);
    }
}

ISR(TIMER0_OVF_vect)
{
    counter += 255;
}

ISR(PCINT0_vect)
{
    if(bit_is_set(PIND, ECHO_PIN))
    {
        TCCR0B |= (1 << CS01); // start timer0, prescaler = 8
        TIMSK0 |= (1 << TOIE0); // enable overflow interrupt
        
        TCNT0 = 0; // initial timer0 value
        //counter = 0;
    }
    else
    {
        cli();
        
        TCCR0B &= ~(1 << CS01); // stop 8 bit timer
        
        counter += TCNT0;
        
        distance = (float)counter / 58.0f / 2.0f;
    }
}

///*------------------------Interrupt PCINT1 for PIN C5 -----------------------------------------*/
//ISR(PCINT1_vect) {
	//if (bit_is_set(PINC,PC5)) {					// Checks if echo is high
		//TCNT1 = 0;								// Reset Timer		
	//} else {
		//uint16_t tnum = TCNT1;					// Save Timer value
		//uint8_t oldSREG = SREG;
		//char buffer[50];						// creating variable buffer
		//
		//cli();									// Disable Global interrupts
//
		//previous_distance = distance;
		//distance = tnum/58/2;
		//
        //SensorData data;
        //data.type = SENSOR_TYPE_DISTANCE;
        //data.data.distance = distance;
        //
        //serialize_sensor_data(&data, buffer);
        //
		//transmit_message(buffer);				// transmitting the distance in cm
//
		//_delay_ms(1000);						// delay so the distance gets send every second
		//SREG = oldSREG;							// Enable interrupts
		//if (distance <= 5){
			//PORTB |= _BV(PB2);
			//PORTB &= ~_BV(PB3);
			//PORTB &= ~_BV(PB1);
		//}										//PB1 = yellow, PB2 = red, PB3 = green
		//else if ((previous_distance - distance) < -1) {//change the -1 to 0 if you don't need the precaution
			//PORTB |= _BV(PB1);					//PinB1 high
			//PORTB |= _BV(PB3);					//PinB3 high
			//PORTB &= ~_BV(PB2);					//PinB2 low
			//_delay_ms(100);
			//PORTB &= ~_BV(PB1);					//PinB1 low
			//_delay_ms(100);
			//PORTB |= _BV(PB1);					//PinB1 High
			//_delay_ms(100);
			//PORTB &= ~_BV(PB1);
			//_delay_ms(100);
			//PORTB |= _BV(PB1);			
		//}
		//else if ((previous_distance - distance) > 1) {	
			//PORTB &= ~_BV(PB3);				//change the 1 to 0 if you don't need the precaution
			//PORTB |= _BV(PB2);
			//PORTB |= _BV(PB1);
			//_delay_ms(100);
			//PORTB &= ~_BV(PB1);
			//_delay_ms(100);
			//PORTB |= _BV(PB1);
			//_delay_ms(100);
			//PORTB &= ~_BV(PB1);
			//_delay_ms(100);
			//PORTB |= _BV(PB1);
		//}
		//else {
			//PORTB |= _BV(PB3);
			//PORTB &= ~_BV(PB2);
			//PORTB &= ~_BV(PB1);
		//}
    //}
//}
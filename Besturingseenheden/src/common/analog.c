#include "analog.h"

#include <avr/io.h>

void init_analog_port(void)
{
    ADMUX = (1 << REFS0);
    
    ADCSRA = (1<<ADEN) | 7;
}

int read_analog_port(void)
{
    ADMUX = (1<<REFS0);  //select input and ref
    ADCSRA |= (1<<ADSC);                 //start the conversion
    while (ADCSRA & (1<<ADSC));          //wait for end of conversion
    return ADCW;
}
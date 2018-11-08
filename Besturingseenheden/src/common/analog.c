#include "analog.h"

#include <avr/io.h>

void init_analog_port(void)
{
    ADMUX = (1 << REFS0);
    ADCSRA = (1<<ADEN) | 7;
}

int read_analog_port(int port)
{
    ADCSRA |= (1 << ADSC) | (1 << port);
    
    loop_until_bit_is_clear(ADCSRA, ADSC);
    return ADCW;
}
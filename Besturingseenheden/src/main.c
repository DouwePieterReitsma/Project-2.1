/*
 * Besturingseenheden.c
 *
 * Created: 2-11-2018 14:27:32
 * Author : dprei
 */ 

#include <avr/io.h>
#define F_CPU 16E6
#include <avr/delay.h>

#include "common/serial.h"
#include "common/analog.h"

int main(void)
{
    initialize_serial_ports();
    initialize_analog_ports();
    
    while (1) 
    {
        transmit_message("Hello World!\n");
        
        _delay_ms(1000);
    }
}
/*
 * serial_communication.c
 *
 * Created: 2-11-2018 15:08:53
 *  Author: dprei
 */ 

#include "serial_communication.h"

#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>

#define F_CPU 16E6
#include <util/delay.h>

#define UBRRVAL 51

void initialize_serial_communication()
{
    //set baud rate
    UBRR0H = 0;
    UBRR0L = UBRRVAL;
    
    //disable U2X mode
    UCSR0A = 0;
    
    //enable transmitter
    UCSR0B= _BV(RXEN0) | _BV(TXEN0);
    
    //set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
    UCSR0C=_BV(UCSZ01)|_BV(UCSZ00);
}

void transmit(uint8_t value)
{
    loop_until_bit_is_set(UCSR0A, UDRE0);
    
    UDR0 = value;
}

uint8_t receive(void)
{
    loop_until_bit_is_set(UCSR0A, RXC0);
    
    return UDR0;
}
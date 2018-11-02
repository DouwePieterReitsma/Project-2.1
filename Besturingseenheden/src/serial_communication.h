/*
 * serial_communication.h
 *
 * Created: 2-11-2018 15:08:19
 *  Author: dprei
 */ 


#ifndef SERIAL_COMMUNICATION_H_
#define SERIAL_COMMUNICATION_H_

void initialize_serial_communication();
void transmit(uint8_t value);
uint8_t receive(void);


#endif /* SERIAL_COMMUNICATION_H_ */
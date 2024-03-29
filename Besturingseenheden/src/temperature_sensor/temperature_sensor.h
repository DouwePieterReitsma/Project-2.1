/*
 * temperature_sensor.h
 *
 * Created: 2-11-2018 15:01:54
 *  Author: dprei
 */ 


#ifndef TEMPERATURE_SENSOR_H_
#define TEMPERATURE_SENSOR_H_

#define TEMPERATURE_ANALOG_PORT 0

void init_temperature_sensor(void);
float get_temperature_in_celsius(void);

// scheduler callback functions
void measure_temperature(void);
void calculate_average_temperature(void);
void transmit_average_temperature(void);


#endif /* TEMPERATURE_SENSOR_H_ */
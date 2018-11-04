/*
 * temperature_sensor.h
 *
 * Created: 2-11-2018 15:01:54
 *  Author: dprei
 */ 


#ifndef TEMPERATURE_SENSOR_H_
#define TEMPERATURE_SENSOR_H_

#define TEMPERATURE_SENSOR_VOLTAGE 5000

void init_temperature_sensor(void);
float get_temperature_in_celsius(void);


#endif /* TEMPERATURE_SENSOR_H_ */
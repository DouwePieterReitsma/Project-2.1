/*
 * temperature_sensor.c
 *
 * Created: 2-11-2018 15:57:44
 *  Author: dprei
 */ 

#include "temperature_sensor.h"
#include "../common/analog.h"

void init_temperature_sensor(void)
{
    init_analog_port();      
}

float get_temperature_in_celsius(void)
{
    int reading = read_analog_port();
    
    float voltage = reading * (5.0f / 1024.0f);
    
    float temperature = (voltage - 0.5f) * 100;
    
    return temperature;
}
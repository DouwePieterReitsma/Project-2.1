/*
 * temperature_sensor.c
 *
 * Created: 2-11-2018 15:57:44
 *  Author: dprei
 */ 

#include "temperature_sensor.h"
#include "../common/analog.h"
#include "../common/serial.h"
#include "../common/sensor_data.h"

#define NUM_TEMPERATURES 40

float temperatures[NUM_TEMPERATURES];

void init_temperature_sensor(void)
{
    init_adc();     
}

float get_temperature_in_celsius(void)
{
    int reading = read_analog_pin(0);
    
    float voltage = reading * (5.0f / 1024.0f);
    
    float temperature = (voltage - 0.5f) * 100;
    
    return temperature;
}

void measure_temperature(void)
{
    static int index = 0;
    
    if(index == NUM_TEMPERATURES)
    {
        index = 0;
    }
    
    temperatures[index] = get_temperature_in_celsius();
    
    index++;
}

void transmit_average_temperature()
{
    char buffer[100];
    float total = 0.0f;
    
    for(int i = 0; i < NUM_TEMPERATURES; i++)
    {
        total += temperatures[i];
    }
    
    
    SensorData data;
    data.type = SENSOR_TYPE_TEMPERATURE;
    //data.data.temperature = get_temperature_in_celsius();
    data.data.temperature = total / NUM_TEMPERATURES;
    
    
    int result = serialize_sensor_data(&data, buffer);
    
    if (result)
    {
        transmit_message(buffer);
    }
}
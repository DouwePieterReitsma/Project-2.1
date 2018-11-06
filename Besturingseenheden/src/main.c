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
#include "common/sensor_data.h"
#include "temperature_sensor/temperature_sensor.h"

int main(void)
{
    char buffer[100];
    
    init_serial_port();
    init_temperature_sensor();
    
    while (1) 
    {
        SensorData data;
        data.type = SENSOR_TYPE_TEMPERATURE;
        data.data.distance = 100;
        data.data.temperature = get_temperature_in_celsius();
        
        int result = serialize_sensor_data(&data, buffer);
        
        transmit_message(buffer);
        
        _delay_ms(1000);
    }
}
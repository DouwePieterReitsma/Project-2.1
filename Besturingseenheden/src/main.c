/*
 * Besturingseenheden.c
 *
 * Created: 2-11-2018 14:27:32
 * Author : dprei
 */ 

#include <avr/io.h>
#define F_CPU 16E6

#include "common/AVR_TTC_scheduler.h"
#include "common/serial.h"
#include "common/analog.h"
#include "common/sensor_data.h"
#include "temperature_sensor/temperature_sensor.h"

void test()
{
    int value = read_analog_pin(1);
    
    char buffer[50];
    
    SensorData data;
    data.type = SENSOR_TYPE_DISTANCE;
    data.data.distance = value;
    
    int result = serialize_sensor_data(&data, buffer);
    
    if (result)
    {
        transmit_message(buffer);
    }
    
}

int main(void)
{
    init_serial_port();
    init_adc();
    init_temperature_sensor();
    SCH_Init_T1();
    
    SCH_Add_Task(&measure_temperature, 0, 100);
    SCH_Add_Task(&transmit_average_temperature, 6000, 6000);
    SCH_Add_Task(&test, 0, 100);
    
    SCH_Start();
    
    while (1) 
    {
        SCH_Dispatch_Tasks();
    }
}
/*
 * Besturingseenheden.c
 *
 * Created: 2-11-2018 14:27:32
 * Author : dprei
 */ 

#include <avr/io.h>
#define F_CPU 16E6

#include <string.h>
#include <avr/delay.h>

#include "common/AVR_TTC_scheduler.h"
#include "common/config.h"
#include "common/serial.h"
#include "common/analog.h"
#include "distance_sensor/distance_sensor.h"
#include "temperature_sensor/temperature_sensor.h"

int main(void)
{
    init_serial_port();
    init_distance_sensor();
    init_temperature_sensor();
    SCH_Init_T1();
       
    SCH_Add_Task(&measure_temperature, 0, 100); // measure temperature every second
    SCH_Add_Task(&calculate_average_temperature, 4000, 4000); // calculate average temperature every 40 seconds
    SCH_Add_Task(&transmit_average_temperature, 6000, 6000); // transmit average temperature every 60 seconds
    //SCH_Add_Task(&measure_distance, 0, 100);
    //SCH_Add_Task(&transmit_distance, 100, 100);
    
    SCH_Start();
    
    while (1) 
    {
        SCH_Dispatch_Tasks();
    }
}
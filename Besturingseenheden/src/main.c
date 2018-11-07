/*
 * Besturingseenheden.c
 *
 * Created: 2-11-2018 14:27:32
 * Author : dprei
 */ 

#include <avr/io.h>
#define F_CPU 16E6
#include <util/delay.h>

#include "common/AVR_TTC_scheduler.h"
#include "temperature_sensor/temperature_sensor.h"

int main(void)
{
    init_serial_port();
    init_temperature_sensor();
    SCH_Init_T1();
    
    // 1 tick = 10ms, 500 * 10ms = 5s
    SCH_Add_Task(&transmit_temperature, 0, 500);
    
    SCH_Start();
    
    while (1) 
    {
        SCH_Dispatch_Tasks();
    }
}
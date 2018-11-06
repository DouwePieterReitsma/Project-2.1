/*
 * sensor_data.h
 *
 * Created: 5-11-2018 15:19:38
 *  Author: dprei
 */ 


#ifndef SENSOR_DATA_H_
#define SENSOR_DATA_H_

typedef enum
{
    ROLLED_IN = 0,
    ROLLED_OUT = 1,
    ROLLING_IN = 2,
    ROLLING_OUT = 3
} SunblindStatus;  

typedef struct
{
    SunblindStatus status;
    
    float temperature;
    
    float light_intensity;
    
    int tick;    
} SensorData;

int serialize_sensor_data(SensorData* data, char* buffer);
int deserialize_sensor_data(const char* str, SensorData* dest);


#endif /* SENSOR_DATA_H_ */
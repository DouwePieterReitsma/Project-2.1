#include "sensor_data.h"

int serialize_sensor_data(SensorData* data, char* buffer)
{
    if (!data)
        return -1;
        
    sscanf(buffer, "%d:%f:%f:%d\n", data->status, data->temperature, data->light_intensity, data->tick);
    
    return 1;
}

int deserialize_sensor_data(const char* data, SensorData* buffer)
{
    
}
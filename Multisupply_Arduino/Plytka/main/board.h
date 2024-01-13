#ifndef BOARD
#define BOARD

#include "Arduino.h"

#include "mcp4021.h"
#include "ina219_voltage.h"
#include "ina219_current.h"

#define MAX_CHANNELS_NUMBER 5
#define PHYSICALL_UNIT_NUMBER 2

#define CURRENT 0
#define VOLTAGE 1

struct _channel{
  MCP4021* pot;
  INA219* meters[PHYSICALL_UNIT_NUMBER];
};

class Board{
    public:
         struct _channel channels[MAX_CHANNELS_NUMBER];
         uint8_t channel, param;
         Board();
         void set(uint8_t value);   
         void inc(void);
         void dec(void);   
         float measure(void);
         void  callib(uint16_t);
         void  config(char * name, uint16_t value);
         float coeff(void);
         uint16_t raw(void);         
};
#endif

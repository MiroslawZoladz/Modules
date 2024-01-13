#ifndef MCP4021_H
#define MCP4021_H
#include "Arduino.h"
#include "non_volatile_float.h"

class MCP4021{
    private:
        uint8_t pin_cs;
        uint8_t state;
        NonVolatileFloat *non_volatile_float; 
        void UD(uint8_t);
        void CS(uint8_t);

    public: 
       MCP4021(uint8_t _potentiometer_cs);
       void inc(uint8_t step_nr);
       void dec(uint8_t step_nr);
       void set(uint8_t step_nr);

       
};
#endif

#ifndef NON_VOLATILE_FLOAT
#define NON_VOLATILE_FLOAT
#include <EEPROM.h>
#include "Arduino.h"

class NonVolatileFloat{
    private:
        static uint8_t obj_counter;
        uint8_t idx_begin;
    public:
         NonVolatileFloat();
         void save(float data);
         float read();
         static void Commit();
};
#endif

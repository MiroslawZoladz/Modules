#include "non_volatile_float.h"
#include <EEPROM.h>

float FloatMockup[5];

NonVolatileFloat::NonVolatileFloat(){
             EEPROM.begin(256);             
             idx_begin = obj_counter*sizeof(float);
             obj_counter++;
}

void NonVolatileFloat::save(float data){

    for(uint8_t current_byte = 0; current_byte < sizeof(float); current_byte++){
        EEPROM.write(idx_begin+current_byte, ((uint8_t *)&data)[current_byte]);
    }
    //EEPROM.commit();
}

float NonVolatileFloat::read(){
    float data = 0;
    for(uint8_t current_byte = 0; current_byte < sizeof(float); current_byte++){
        ((uint8_t *)&data)[current_byte] = EEPROM.read(idx_begin+current_byte);
    }
    return data;    
}

void NonVolatileFloat::Commit(void){
    EEPROM.commit();
}

uint8_t NonVolatileFloat::obj_counter = 0;

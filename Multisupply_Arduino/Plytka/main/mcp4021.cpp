#include "mcp4021.h"
#define PIN_UD 14

MCP4021::MCP4021(uint8_t _pin_cs){
    pin_cs = _pin_cs;
    non_volatile_float = new NonVolatileFloat();
    state = 0;
    
    pinMode(PIN_UD, OUTPUT);
    pinMode(pin_cs, OUTPUT);
    
    set(non_volatile_float->read());   
}

void MCP4021::UD(uint8_t state) {
    digitalWrite(PIN_UD, state);
};

void MCP4021::CS(uint8_t state){
    digitalWrite(pin_cs, state);
};

 void MCP4021::dec(uint8_t step_nr){
    CS(HIGH);
    UD(HIGH);
    CS(LOW);    
    for(uint8_t i = 0; i < step_nr; i++) {
       UD(LOW);
       UD(HIGH);
       if (state>0) state--;
    }  
    CS(HIGH);
    non_volatile_float->save(state);
 } 

 void MCP4021::inc(uint8_t step_nr){
    CS(HIGH);
    UD(LOW);
    CS(LOW);    
    for(uint8_t i = 0; i < step_nr; i++) {
       UD(HIGH);
       UD(LOW);
       if (state<63) state++;       
    } 
    CS(HIGH); 
    non_volatile_float->save(state);
 } 
  
void MCP4021::set(uint8_t value){ 
   dec(64);
   inc(value);
  // non_volatile_float->Commit();
} 

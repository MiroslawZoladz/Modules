#ifndef INA219_H
#define INA219_H

#include <Wire.h>
#include "Arduino.h"
#include <Adafruit_BusIO_Register.h>
#include <Adafruit_I2CDevice.h>
#include "non_volatile_float.h"

class INA219{ 
   private:
      Adafruit_BusIO_Register *config_reg;
      NonVolatileFloat *callib_coeff;    
      uint16_t cfg_sadc, cfg_badc, cfg_pg, cfg_brng;            
   protected:
      Adafruit_BusIO_Register *voltage_reg;      
      uint8_t voltage_val_bp;
   public: 
      INA219(Adafruit_I2CDevice *i2c_dev); 
      
      uint16_t measure_raw();
      void callib(float measured_mili);
      void config(char *bit_field, uint16_t field_value);
      float read_coefficient();
      float measure();
};

#endif

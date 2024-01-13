#ifndef INA219_VOLTAGE_H
#define INA219_VOLTAGE_H
#include "ina219.h"

class INA219_Voltage : virtual public INA219{
   public:
      INA219_Voltage(Adafruit_I2CDevice *i2c_dev);
};

#endif

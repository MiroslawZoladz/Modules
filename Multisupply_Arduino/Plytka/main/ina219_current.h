#ifndef INA_CURRENT_H
#define INA_CURRENT_H
#include "ina219.h"

class INA219_Current : virtual public INA219{
   public:
      INA219_Current(Adafruit_I2CDevice *i2c_dev);
};

#endif

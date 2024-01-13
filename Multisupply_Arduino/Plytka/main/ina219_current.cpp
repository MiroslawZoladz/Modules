#include "ina219_current.h"

#define INA219_REG_SHUNTVOLTAGE (0x01)

INA219_Current::INA219_Current(Adafruit_I2CDevice *i2c_dev):INA219(i2c_dev){    
    voltage_reg = new Adafruit_BusIO_Register(i2c_dev, INA219_REG_SHUNTVOLTAGE , 2, MSBFIRST);
    voltage_val_bp = 0;
}

#include "ina219_voltage.h"

#define INA219_REG_BUSVOLTAGE (0x02)

INA219_Voltage::INA219_Voltage(Adafruit_I2CDevice *i2c_dev):INA219(i2c_dev){
    voltage_reg = new Adafruit_BusIO_Register(i2c_dev, INA219_REG_BUSVOLTAGE, 2, MSBFIRST);
    voltage_val_bp = 3;
}

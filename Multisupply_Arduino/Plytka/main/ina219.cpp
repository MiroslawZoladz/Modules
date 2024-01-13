#include "ina219.h"

#define DEFAULT_CONFIG (0x7FF)
#define INA219_CONFIG_MODE_SANDBVOLT_CONTINUOUS (0x07)
#define INA219_REG_CONFIG (0x00)

INA219::INA219(Adafruit_I2CDevice *i2c_dev){
        config_reg  =  new Adafruit_BusIO_Register(i2c_dev, INA219_REG_CONFIG, 2, MSBFIRST);   
        callib_coeff = new NonVolatileFloat();  

        cfg_sadc = 0xF;
        cfg_badc = 0xF;
        cfg_pg   = 0x0;
        cfg_brng = 0x0;
}

void INA219::config(char *name, uint16_t value){         

    if(strcmp(name, "sadc") == 0){
        cfg_sadc = value;
    }
    else if(strcmp(name, "badc") == 0){
        cfg_badc = value;
    }
    else if(strcmp(name, "pg") == 0){
        cfg_pg = value;
    }
    else if(strcmp(name, "brng") == 0){
        cfg_brng = value;
    }
    else{
        Serial.println("err");
    }
}

float INA219::measure(){
    return (measure_raw()*callib_coeff->read());
}  

uint16_t INA219::measure_raw(){
    uint16_t reg_value;     
    uint16_t config_value = ((cfg_brng<< 13) | (cfg_pg << 11) | (cfg_badc << 7) | (cfg_sadc << 3) | INA219_CONFIG_MODE_SANDBVOLT_CONTINUOUS);
    config_reg->write(config_value, 2);
    voltage_reg->read(&reg_value);         
    return (reg_value >> voltage_val_bp);
}

void INA219::callib(float measured_mili){
     callib_coeff->save(measured_mili/measure_raw());
}
       
float INA219::read_coefficient(){
    return callib_coeff->read();
}

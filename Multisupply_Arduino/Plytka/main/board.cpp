#include "board.h"


#define CURRENT 0
#define VOLTAGE 1

Board::Board(){
  uint8_t channel_cs[MAX_CHANNELS_NUMBER] = {18, 22, 28, 27, 26};
  uint8_t channel_address[MAX_CHANNELS_NUMBER] = {0x44, 0x43, 0x42, 0x41, 0x40};
  
  for(int ch_counter = 0; ch_counter < MAX_CHANNELS_NUMBER; ch_counter++){
    channels[ch_counter].pot = new MCP4021(channel_cs[ch_counter]);    

    Adafruit_I2CDevice* i2c_dev = new Adafruit_I2CDevice(channel_address[ch_counter], &Wire);
    i2c_dev->begin();

    channels[ch_counter].meters[CURRENT] = new INA219_Current(i2c_dev);
    channels[ch_counter].meters[VOLTAGE] = new INA219_Voltage(i2c_dev);         
  }
  
  channel = 0;
  param = VOLTAGE;
};


void  Board::set(uint8_t value){ channels[channel].pot->set(value);}
void  Board::inc(void){ channels[channel].pot->inc(1);}
void  Board::dec(void){ channels[channel].pot->dec(1);}
float Board::measure(void)   {return channels[channel].meters[param]->measure();}
void  Board::callib(uint16_t value) {channels[channel].meters[param]->callib(value);}
void  Board::config(char * name, uint16_t value) {channels[channel].meters[param]->config(name, value);}
float Board::coeff(void)   {return channels[channel].meters[param]->read_coefficient();}
uint16_t Board::raw(void)   {return channels[channel].meters[param]->measure_raw();}

//      case R: printval(channels[active_channel].meters[active_parameter]->measure_raw());break;

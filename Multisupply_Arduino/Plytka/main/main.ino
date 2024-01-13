#include <Wire.h>

#include "board.h"
#include "my_display.h"
#include "keyboard.h"
#include "non_volatile_float.h"
          
Board * board;
MyDisplay display;
Keyboard keyboard;

void setup(void) 
{
  Wire.setSDA(20);
  Wire.setSCL(21);
  Wire.begin();
  Wire.setClock(100000); //100kHz

  board = new Board();
  display.Init();
}

uint8_t channel = 0;

void loop(void) 
{  
  switch (keyboard.eRead()) {
    case UP:     if (board->channel < 4) board->channel++; break;    
    case DOWN:   if (board->channel > 0) board->channel--; break;
    case RIGHT:  board->inc();break;
    case LEFT:   board->dec(); break;
    case MIDDLE: NonVolatileFloat::Commit(); break;
    default: break;    
  }

  board->param = VOLTAGE;
  float voltage = board->measure();
  
  board->param = CURRENT;
  float current = board->measure();
  if (current > 10000) current = 0;
  
  display.Show(board->channel, voltage/1000, current/1000);
  
  delay(50);  
}

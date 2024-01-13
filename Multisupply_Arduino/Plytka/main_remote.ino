#include <Wire.h>

#include "ina219_voltage.h"
#include "ina219_current.h"
#include "command_decoder.h"
#include "string.h"
#include "mcp4021.h"
#include "my_display.h"
#include "board.h"
#include "non_volatile_float.h"
#include "help.h"
             
String s_command;
Board * board;
MyDisplay Display;

void printval(float read_value){
  Serial.print(String(read_value, 10));
};

void setup(void) 
{
  Wire.setSDA(20);
  Wire.setSCL(21);
  Wire.begin();
  Wire.setClock(100000); //100kHz

  Serial.setTimeout(-1);
  Serial.begin(9600);

  board = new Board();

  Display.Init();
}

void loop(void) 
{
  float val;
  
  char ac_command[MAX_COMMAND_LTH];
  s_command = Serial.readStringUntil('\r');
  s_command.toCharArray(ac_command, MAX_COMMAND_LTH);
  decode_msg(ac_command);

  if((token_no > 0) & (as_token[0].type == KEYWORD)){
    switch(as_token[0].value.as_keyword){
      case CH: board->channel = as_token[1].value.number; break;
      case V: board->param = VOLTAGE; break;
      case C: board->param = CURRENT;  break;
      case S: board->set(as_token[1].value.number); break;   
      case M: 
           val = board->measure();
           if (val > 10000) val = 0;
           printval( val);
      break;
      case L: board->callib(int(as_token[1].value.number));break;
      case G: board->config(as_token[1].value.pc_str, as_token[2].value.number); break;
      case F: printval(board->coeff());break;  
      case R: printval(board->raw());break;
      case A: NonVolatileFloat::Commit();break;
      default: Serial.print(HELP);      
    }
    Serial.println(" ok");
  }
  else{
     Serial.print(HELP);  
   }
}

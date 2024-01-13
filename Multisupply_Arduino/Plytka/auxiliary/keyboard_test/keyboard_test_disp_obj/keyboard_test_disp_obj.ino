#include <Wire.h>
#include "my_display.h"
enum KeyboardState {RELEASED, UP, DOWN, LEFT, RIGHT, MIDDLE};
                            //   4, 0,    3      2    1 

enum KeyboardState eReadButtons(void)
{
  if(0 == digitalRead(4)) return UP;
  if(0 == digitalRead(0)) return DOWN;
  if(0 == digitalRead(3)) return LEFT;
  if(0 == digitalRead(2)) return RIGHT;    
  if(0 == digitalRead(1)) return MIDDLE;
  return RELEASED;          
}

MyDisplay Display;

 //=======================================================================
void setup()
{
  Wire.setSDA(20);
  Wire.setSCL(21);
  Wire.begin();
  Wire.setClock(400000); //400kHz

  Display.Init();

  pinMode(0, INPUT_PULLUP);
  pinMode(1, INPUT_PULLUP);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
}
 

//=======================================================================
void test(void) 
{

}


//=======================================================================
 void loop() 
 {

    
    while(1) {
      Display.Show(0, 1.234, 4.567);
      delay(100);
      Display.Show(1, 0.234, 0.567);
      delay(100);
      Display.Show(4, 1.230, 4.569);
      delay(100);    
    }
}

#ifndef KEYBOARD
#define KEYBOARD

#include "Arduino.h"

enum KeyboardState {RELEASED, UP, DOWN, LEFT, RIGHT, MIDDLE};
                            //   4, 0,    3      2    1 
                            
class Keyboard{
    public:
         Keyboard();
         enum KeyboardState eCurrentKeyboardState,ePreviousKeyboardState;
         enum KeyboardState eReadButtons(void);
         enum KeyboardState eRead(void);
         
         
};
#endif

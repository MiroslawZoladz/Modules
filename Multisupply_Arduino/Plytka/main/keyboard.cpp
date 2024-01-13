#include "keyboard.h"

Keyboard::Keyboard(void)
{
  pinMode(0, INPUT_PULLUP);
  pinMode(1, INPUT_PULLUP);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
}

enum KeyboardState Keyboard::eReadButtons(void)
{
  if(0 == digitalRead(4)) return UP;
  if(0 == digitalRead(0)) return DOWN;
  if(0 == digitalRead(3)) return LEFT;
  if(0 == digitalRead(2)) return RIGHT;    
  if(0 == digitalRead(1)) return MIDDLE;
  return RELEASED;          
}

enum KeyboardState Keyboard::eRead(void)
{           
   enum KeyboardState result = RELEASED;

   eCurrentKeyboardState=eReadButtons();
   if ((eCurrentKeyboardState !=	RELEASED) && (ePreviousKeyboardState ==	RELEASED)){
         result = eCurrentKeyboardState;
   }
   ePreviousKeyboardState=eCurrentKeyboardState;				

   return result;
}

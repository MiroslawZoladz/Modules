#ifndef MY_DISPLAY
#define MY_DISPLAY


#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Fonts/FreeSans12pt7b.h> 

#include "Arduino.h"

class MyDisplay{
    public:
         MyDisplay();
         Adafruit_SSD1306 * oled; //(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
         void Init(void);
         void Show(byte section, float voltage, float current);
};
#endif

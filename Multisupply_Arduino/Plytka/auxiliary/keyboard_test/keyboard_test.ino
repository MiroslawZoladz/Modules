/*=================================================================
# Project : I2C OLED (SSD1306)
#         : 
# Date    : 2021-04-09
# Version : 1.3
#
# Note:
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY : without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE
#
# Board : Raspberry Pi Pico
# IDE   : Arduino IDE
# Library :
#     Adafruit_SSD1306 : https://github.com/adafruit/Adafruit_SSD1306
#     Adafruit_GFX     : https://github.com/adafruit/Adafruit-GFX-Library
#=================================================================*/
 
#include <Wire.h>
 
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Fonts/FreeSans9pt7b.h> 

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
// The pins for I2C are defined by the Wire-library. 
// On an arduino UNO:       A4(SDA), A5(SCL)
// On an arduino MEGA 2560: 20(SDA), 21(SCL)
// On an arduino LEONARDO:   2(SDA),  3(SCL), ...
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3c // i2c slave address
Adafruit_SSD1306 oled(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);



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

 
 
 //=======================================================================
void setup()
{
  Wire.setSDA(20);
  Wire.setSCL(21);
  Wire.begin();
  Wire.setClock(400000); //400kHz

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!oled.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
  }
  
  oled.display();
  
  oled.setTextSize(1);      // Normal 1:1 pixel scale
  oled.setTextColor(SSD1306_WHITE); // Draw white text
  oled.cp437(true);         // Use full 256 char 'Code Page 437' font    
  oled.setFont(&FreeSans9pt7b);

  pinMode(0, INPUT_PULLUP);
  pinMode(1, INPUT_PULLUP);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
}
 

//=======================================================================
void test(void) 
{
    
    oled.clearDisplay();
    
    oled.setCursor(0, 38);   
    oled.write("DISC");
    
    oled.setCursor(56, 25);   

    char buff[10];
    dtostrf((float)eReadButtons(),5,3,buff);
    oled.write(buff);
    oled.setCursor(64, 50);
    oled.write("0.567 A");
    
    oled.display();

}


//=======================================================================
 void loop() 
 {
    
    while(1) {
    test();
    delay(100);
    }
}

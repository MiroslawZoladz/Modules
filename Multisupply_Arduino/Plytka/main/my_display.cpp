#include "my_display.h"
#include <Wire.h>

#define SCREEN_WIDTH 128 
#define SCREEN_HEIGHT 64 

#define SCREEN_ADDRESS 0x3c // i2c slave address
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)

MyDisplay::MyDisplay(){
  oled = new Adafruit_SSD1306(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
}

void MyDisplay::Init(void){

  if(!oled->begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
  }
  
  oled->display();
  
  oled->setTextSize(1);      // Normal 1:1 pixel scale
  oled->setTextColor(SSD1306_WHITE); // Draw white text
  oled->cp437(true);         // Use full 256 char 'Code Page 437' font    
  oled->setFont(&FreeSans12pt7b);

  oled->clearDisplay();
  
  oled->setCursor(0, 38);   
  oled->write("REMOTE");
  oled->display();

}
void MyDisplay::Show(byte section, float voltage, float current){

   
    const char *sections[5] = {"core","peri","ddm","dda","disc"};
  
    oled->clearDisplay();
    
    oled->setCursor(0, 38);   
    oled->write(sections[section]);

    char buff[10];
    
    oled->setCursor(48, 25);   
    dtostrf(voltage,5,3,buff);
    buff[5] = ' ';
    buff[6] = 'V';
    buff[7] = 0;
    oled->write(buff);
    
    oled->setCursor(48, 50);
    dtostrf(current,5,3,buff);
    buff[5] = ' ';
    buff[6] = 'A';
    buff[7] = 0;
    oled->write(buff);
    
    oled->display();
  
  };

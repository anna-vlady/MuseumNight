#ifndef BOARD_HAS_PSRAM
#error "Please enable PSRAM!"
#endif

#include <Arduino.h>
#include "epd_driver.h"

#include "src/pic1.h"
#include "utilities.h"

void setup()
{
    Serial.begin(115200);

    epd_init();

    Rect_t area = {
        .x = 0,
        .y = 0,
        .width = pic1_width,
        .height = pic1_height
    };

    epd_poweron();

    epd_clear();

    epd_draw_grayscale_image(
        area,
        (uint8_t *)pic1_data
    );

    epd_poweroff();
}

void loop()
{
    // Do nothing
}
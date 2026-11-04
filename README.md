# Museum Night

Shows images on a 4.7 inch LilyGo T5 ePaper S3 screen (960 x 540, ESP32 S3).

Python scripts prepare each picture for the screen. They resize it, adjust it, convert it to 16 level grayscale and write the pixels into a C header file. An Arduino sketch then compiles that header into the firmware and draws the image on the display.

## What is in this repo

**Image scripts**: `simple.py`, `my1.py`, `convert.py`, plus the scripts in `cross gif` and `ararat images`. Each one is a small variation on the same conversion with its own size, rotation, contrast or brightness settings. `convert.py` is the exception, as it makes a 200 x 200 black and white bitmap.

**Arduino sketches**: `lilygo screen` has a sketch that loops through three images, changing every 3 seconds. The drawImages example in the LilyGo folder has been edited to draw one image and then hold it.

**Images**: the source pictures and generated headers, including the Abovian portrait, book and quill, Ararat and cross images.

**LilyGo library**: a copy of the display driver and examples from LilyGo, under its GPL 3 license.

## How to use it

1. Install Pillow with `pip install pillow`.
2. Set the input image name in a script, then run it from that script's folder to create `pic1.h`.
3. Copy the header into the `src` folder of the drawImages example.
4. Install the LilyGo library in the Arduino IDE, then select the ESP32S3 Dev Module board with OPI PSRAM enabled.
5. Open the sketch and upload it to the board.

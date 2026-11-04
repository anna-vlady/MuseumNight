from PIL import Image

# Open image
img = Image.open("Abovianportrait.jpg")

# Resize to e-paper resolution
img = img.resize((200, 200))

# Convert to black/white with dithering
img = img.convert("1", dither=Image.FLOYDSTEINBERG)

pixels = img.load()

data = []

# Pack 8 pixels into 1 byte
for y in range(img.height):

    for x in range(0, img.width, 8):

        byte = 0

        for b in range(8):

            if x + b < img.width:

                pixel = pixels[x + b, y]

                # Black pixel
                if pixel == 0:
                    byte |= (1 << (7 - b))

        data.append(byte)

# Write Arduino header file
with open("image.h", "w") as f:

    f.write("#pragma once\n\n")
    f.write("#include <pgmspace.h>\n\n")

    f.write("const unsigned char myBitmap[] PROGMEM = {\n")

    for i, b in enumerate(data):

        if i % 16 == 0:
            f.write("\n")

        f.write(f"0x{b:02X}, ")

    f.write("\n};\n")

print("image.h created successfully!")

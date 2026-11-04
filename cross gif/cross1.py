from PIL import Image

# Open image
img = Image.open("cross7.png")

# Rotate image vertical
img = img.rotate(90, expand=True)

# Stretch to display resolution
img = img.resize((960, 540))

# Convert to grayscale
img = img.convert("L")

pixels = img.load()

data = []

for y in range(img.height):

    for x in range(0, img.width, 2):

        p1 = pixels[x, y] >> 4
        p2 = pixels[x + 1, y] >> 4

        byte = (p1 << 4) | p2

        data.append(byte)

with open("pic1.h", "w") as f:

    f.write("#pragma once\n\n")

    f.write(f"const uint32_t pic1_width = {img.width};\n")
    f.write(f"const uint32_t pic1_height = {img.height};\n\n")

    f.write("const uint8_t pic1_data[] = {\n")

    for i, b in enumerate(data):

        if i % 16 == 0:
            f.write("\n")

        f.write(f"0x{b:02X}, ")

    f.write("\n};\n")

print("pic1.h created successfully!")

from PIL import Image

# Open image
img = Image.open("cross1.png")

# Rotate image vertical
img = img.rotate(90, expand=True)

# Resize to vertical screen
img = img.resize((540, 960))

# Convert to grayscale
img = img.convert("L")

pixels = img.load()

data = []

# Pack two 4-bit pixels into one byte
for y in range(img.height):

    for x in range(0, img.width, 2):

        p1 = pixels[x, y] >> 4
        p2 = pixels[x + 1, y] >> 4

        byte = (p1 << 4) | p2

        data.append(byte)

# Write .h file
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

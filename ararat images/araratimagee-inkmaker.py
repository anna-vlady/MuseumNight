from PIL import Image, ImageEnhance, ImageFilter, ImageOps

# Open image
# img = Image.open("aaa.jpg")
#img = Image.open("bbb.png")
#img = Image.open("ccc.png")
#img = Image.open("ddd.png")
img = Image.open("bookandquill.png")

# Rotate for portrait orientation
# img = img.rotate(90, expand=True)

# Stretch to fill full e-ink display
img = img.resize((960, 540))

# Increase contrast
contrast = ImageEnhance.Contrast(img)
img = contrast.enhance(2)

# Slight brightness boost
brightness = ImageEnhance.Brightness(img)
img = brightness.enhance(1)

# Sharpen image
img = img.filter(ImageFilter.SHARPEN)

# Convert to grayscale
img = img.convert("L")

# Auto-adjust black/white levels
img = ImageOps.autocontrast(img)

# Optional invert
# Uncomment next line if desired
# img = ImageOps.invert(img)

pixels = img.load()

data = []

# Pack two 4-bit grayscale pixels into one byte
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

from PIL import Image
import numpy as np
import time
import os

s = time.time()

for f in os.listdir("./input/"):
    img = Image.open("./input/" + f)
    convert = {
        "#000000": "#AAAAAA",
        "#000000": "#AAAAAA",
        "#000000": "#AAAAAA",
        "#000000": "#AAAAAA",
        "#000000": "#AAAAAA"
    }

    data = np.array(img)

    def hex2rgb(h):
        return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) # skip '#'

    def rgb2hex(r, g, b):
        return ("#{:02x}{:02x}{:02x}".format(r, g, b)).upper()

    for row in range(len(data)):
        for pixel in range(len(data[row])):
            p = data[row][pixel]
            if p[3] == 255:
                pixel_hex = rgb2hex(p[0], p[1], p[2])
                for i in convert:
                    if pixel_hex == i:
                        pixel_rgb = hex2rgb(convert[i])
                        data[row][pixel] = [pixel_rgb[0], pixel_rgb[1], pixel_rgb[2], 255]

    Image.fromarray(data).save("./output/" + f)

print(f"Finished in {time.time() - s} seconds")
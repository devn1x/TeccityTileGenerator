import os
import sys
from PIL import Image

config_heading = sys.argv[1] # One of "ne", "nw", "se", "sw"
config_path_source = "../TeccityImages/output-{heading}.png"
config_path_output = "../TeccityImages/tiles-{heading}/{z}/{x}/{y}.png"
config_zoom_max = 6

def prepare_map_image() -> Image.Image:
    # Crop image to it's maximum square
    print(f"prepare map for heading {config_heading}")
    img = Image.open(config_path_source.format_map({'heading': config_heading}))
    width, height = img.size

    box = ((width - height) / 2, 0, (width - height) / 2 + height, height)

    return img.crop(box)

def generate_tile(x, y, z):
    path = config_path_output.format_map({'x': x, 'y': y, 'z': z, 'heading': config_heading})
    os.makedirs(os.path.dirname(path), exist_ok=True)
    width, height = img.size

    left = width / pow(2, z) * x
    top = height / pow(2, z) * y
    right = left + (width / pow(2, z))
    bottom = top + (height / pow(2, z))

    box = (left, top, right, bottom)
    tile = img.crop(box)

    tile.thumbnail((512,512), Image.Resampling.NEAREST)
    tile.save(path)

img = prepare_map_image()

for z in range(0, config_zoom_max + 1):
    print(f"zoom level {z}")
    for y in range(0, pow(2, z)):
        for x in range(0, pow(2, z)):
            generate_tile(x, y, z)
from PIL import Image, ImageChops

############################################# split and compare

a = Image.open('./A.png').convert("RGB")
c = Image.open('./C.png').convert("RGB")

import numpy as np


def percent_same(a, b):
    np_a = np.array(a)
    np_b = np.array(b)
    return np.mean(np_a == np_b)


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0))).convert("RGB")
    diff = ImageChops.difference(im, bg).convert("RGB")
    diff = ImageChops.add(diff, diff, 2.0, -100).convert("RGB")
    # Bounding box given as a 4-tuple defining the left, upper, right, and lower pixel coordinates.
    # If the image is completely empty, this method returns None.
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)


def left_side(x):  # split image and return only right side
    width, height = x.size
    return trim(x.crop((0, 0, width / 2, height)))


def right_side(x):  # split image and return only left side
    width, height = x.size
    return trim(x.crop((width / 2, 0, width, height)))


left = left_side(a)
right = right_side(c)

print(percent_same(left, right))  # ths should be at least .95 but instead returns 0.0

left_side(a)
diff = ImageChops.difference(left, right)

if diff.getbbox():
    print("images are different")
else:
    print("images are the same")

left.show()
right.show()

import numpy as np
import math
import random


width = 8
height = 8


def random_pixel_generator(width, height):
    image = np.zeros((height, width))
    for i in range(height):
        for j in range(width):        image[i, j] = int(random.random()*100)

    return image


image = random_pixel_generator(width, height)

print(image)
def generate_8x8_image():
    """Generates an 8x8 pixel image as a NumPy array"""

    # Create empty 8x8 array
    image = np.zeros((8, 8))

    # Set pixel values here
    image[0, 0] = 1
    image[1, 1] = 1
    image[7, 7] = 1

    return image


image = generate_8x8_image()
print(image)

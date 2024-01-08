<<<<<<< HEAD
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np

width = 8
height = 8
batch_size = 16
=======
import numpy as np
import math
import random


width = 8
height = 8
>>>>>>> 2131ae465e76497be117a5bff8d1c1e3ab84996b


def random_pixel_generator(width, height):
    image = np.zeros((height, width))
    for i in range(height):
<<<<<<< HEAD
        for j in range(width):        image[i, j] = int(torch.rand(1)*2)
    print(image)
    return image


t1 = torch.as_tensor(random_pixel_generator(width, height))
print(t1)

=======
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
>>>>>>> 2131ae465e76497be117a5bff8d1c1e3ab84996b

import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np

width = 8
height = 8


def random_pixel_generator(width, height):
    image = np.zeros((height, width))
    for i in range(height):

        for j in range(width):        image[i, j] = int(torch.rand(1)*2)
    print(image)
    return image


t1 = torch.as_tensor(random_pixel_generator(width, height))
print(t1)




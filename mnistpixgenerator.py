import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import numpy as np
from PIL import Image

data = np.random.randint(0, 2, size=(28, 28))

# Scale data to 0-255 range
data = (data * 255).astype(np.uint8)

img = Image.fromarray(data, 'L')
img.save('image.png')
t1 = torch.as_tensor(data, dtype=torch.float32)
print(t1.size())
mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
mnist_testset = datasets.MNIST(root='./data', train=False, download=True, transform=None)
t2len = len(mnist_testset)


# def random_pixel_generator(width, height):
#    image = np.zeros((height, width))
#    for i in range(height):
#        for j in range(width):        image[i, j] = int(torch.rand(1)*2)
#    print(image)
#   return image
#

# t1 = torch.as_tensor(random_pixel_generator(width, height))




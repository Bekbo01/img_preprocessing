import cv2
import numpy as np
import os
import skimage.color
import skimage.io
import matplotlib.pyplot as plt


IMAGE_PATH = "kazakh_alphabet/a/0.png"

DATASET = 'kazakh_alphabet'
files = []
for name in os.listdir(DATASET):
    if '.' not in name:
        files += [DATASET + '/' + name + '/' + n for n in os.listdir(DATASET + '/' + name) if n[-4:] == '.png']


image = skimage.io.imread(fname=files[0], as_gray=True)
histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))

for i in range(1, len(files)):
    image = skimage.io.imread(fname=files[i], as_gray=True)
    hist, bin_edges = np.histogram(image, bins=256, range=(0, 1))
    histogram += hist

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([0.0, 1.0])
plt.plot(bin_edges[0:-1], histogram)
plt.show()
plt.savefig('hist.png')


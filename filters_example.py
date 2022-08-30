import cv2
import numpy as np
from scipy.signal import wiener

IMAGE_PATH = "kazakh_alphabet/a/0.png"

img = cv2.imread(IMAGE_PATH)
print(img.shape)
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
wiener_img = wiener(img, (5, 5))

cv2.imshow('Original', img)
cv2.imshow('Gaussian', gaussian)
cv2.imshow('Median', median)
cv2.imshow('Wiener', wiener_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

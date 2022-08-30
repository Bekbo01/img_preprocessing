import cv2
import numpy as np
import skimage

IMAGE_PATH = "kazakh_alphabet/a/0.png"
img = cv2.imread(IMAGE_PATH)

gaussian_noise_img1 = skimage.util.random_noise(img, mode='gaussian',
                                               mean=0, var=0.01)

gaussian_noise_img2 = skimage.util.random_noise(img, mode='gaussian',
                                               mean=0.2, var=0.01)

salt_paper_noise_img = skimage.util.random_noise(img, mode='s&p',
                                                 amount=0.02)

cv2.imshow('Original', img)
cv2.imshow('Gaussian noise mean=0, var=0.01', gaussian_noise_img1)
cv2.imshow('Gaussian noise mean=0.2, var=0.01', gaussian_noise_img2)
cv2.imshow('Salt & Pepper noise amount=0.02', salt_paper_noise_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

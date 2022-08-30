import cv2
import numpy as np

IMAGE_PATH = "kazakh_alphabet/a/0.png"

def bernsen(img):
    h, w = img.shape
    img1 = np.zeros((h, w), np.uint8)
    for i in range(1, h-1):
        for j in range(1, w-1):
            matrix = np.zeros((3, 3), np.uint8)
            for k in range(-1, 2):
                for l in range(-1, 2):
                    matrix[k+1, l+1] = img[i+k, j+l]
            threshold = (np.max(matrix) + np.min(matrix))/2
            if img[i, j] >= threshold:
                img1[i, j] = 255
            else:
                img1[i, j] = 0
    return img1

img = cv2.imread(IMAGE_PATH)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

th, otsu_gray_img = cv2.threshold(gray, 110, 200, cv2.THRESH_OTSU)
adaptive_gray_img = cv2.adaptiveThreshold(gray, 200,\
                                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                               cv2.THRESH_BINARY, 11, 2)
bernsen_gray_img = bernsen(gray)

cv2.imshow('Original', img)
cv2.imshow('Gray', gray)
cv2.imshow('Otsu', otsu_gray_img)
cv2.imshow('Adaptive', adaptive_gray_img)
cv2.imshow('Bernsen', bernsen_gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

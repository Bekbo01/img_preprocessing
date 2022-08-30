import cv2
import numpy as np
import skimage

IMAGE_PATH = "kazakh_alphabet/a/68.png"
img = cv2.imread(IMAGE_PATH)

lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

lab_img_2d = lab_img.reshape((-1,3))
lab_img_2d = np.float32(lab_img_2d)
n_rows, n_cols, _ = img.shape

k = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_PP_CENTERS

_, ids, centers = cv2.kmeans(lab_img_2d, k, None, criteria, 10, flags)
center = np.uint8(centers)
res = center[ids.flatten()]
result_image = res.reshape((img.shape))

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
#canny
img_canny = cv2.Canny(img,100,200)
#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely
#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
img_prewitt = img_prewittx + img_prewitty

cv2.imshow('Original', img)
cv2.imshow('result_image k=3', result_image)
cv2.imshow('img_canny', img_canny)
cv2.imshow('img_sobel', img_sobel)
cv2.imshow('img_sobelx', img_sobelx)
cv2.imshow('img_prewittx', img_prewittx)
cv2.imshow('img_prewitt', img_prewitt)
cv2.waitKey(0)

cv2.destroyAllWindows()

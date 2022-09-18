import cv2 as cv
import numpy as nm

#membaca img dan di convert menjadi warna grayscale
img=cv.imread('test_img.jpg')
imgBright = cv.imread('test_img.jpg')
grayScaleImg=cv.cvtColor(img,cv.IMREAD_GRAYSCALE)


#brightness dilakukan
alpha = 2.0 # Contrast control (1.0-3.0)
beta = 20 # Brightness control (0-100)

adjusted = cv.convertScaleAbs(img, alpha=alpha, beta=beta)

cv.imshow('original',img)
cv.imshow('Brightnes and contrast',adjusted)



cv.waitKey(0)
cv.destroyAllWindows()         

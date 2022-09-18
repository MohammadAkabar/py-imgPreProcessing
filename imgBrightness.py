import cv2 as cv
import numpy as nm

#membaca img dan di convert menjadi warna grayscale
img=cv.imread('test_img.jpg')
imgBright = cv.imread('test_img.jpg')
grayScaleImg=cv.cvtColor(img,cv.IMREAD_GRAYSCALE)


#brightness dilakukan
alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

#fungsi untuk mengubah brightness
adjusted = cv.convertScaleAbs(img, alpha=alpha, beta=beta)

#menampilkan hasil citra
cv.imshow('original',img)
cv.imshow('Brightness',adjusted)



cv.waitKey(0)
cv.destroyAllWindows()         

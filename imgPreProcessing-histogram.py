import cv2 as cv
import numpy as nm
import matplotlib.pyplot as plt

#membaca img dan di convert menjadi warna grayscale

img=cv.imread('test_img.jpg',0)
grayScaleImg=cv.cvtColor(img,cv.IMREAD_GRAYSCALE)

#mengconvert ke histogram
plt.hist(img.ravel(),256,[0,256]); plt.show()


cv.waitKey(0)
cv.destroyAllWindows()    

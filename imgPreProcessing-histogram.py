import cv2 as cv
import numpy as nm
import matplotlib.pyplot as plt

#membaca img 
img=cv.imread('test_img.jpg')


#mengconvert ke histogram
plt.hist(img.ravel(),256,[0,256]); plt.show()


cv.waitKey(0)
cv.destroyAllWindows()    

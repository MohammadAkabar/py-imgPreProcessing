import cv2 as cv
import numpy as np

img = cv.imread('test_img.jpg')
inverted = np.invert(img)

cv.imshow('inverted.jpg', inverted)

cv.waitKey(0)
cv.destroyAllWindows()

import cv2
import numpy as nm

#membaca img dan di convert menjadi warna grayscale
img=cv2.imread('test_img.jpg')
grayScaleImg=cv2.cvtColor(img,cv2.IMREAD_GRAYSCALE)


ret, bw_img = cv2.threshold(grayScaleImg,127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary Image",bw_img)

cv2.waitKey(0)
cv2.destroyAllWindows()         

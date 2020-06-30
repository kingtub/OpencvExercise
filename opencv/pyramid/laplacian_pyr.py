'''
拉普拉斯金字塔。用来还原图像的
'''
import cv2

o = cv2.imread('C:\\D\\testImgs\\chapter12\\image\\girl.bmp', cv2.IMREAD_UNCHANGED)
od = cv2.pyrDown(o)
odu = cv2.pyrUp(od)

laplacianPyr = o - odu
back = odu + laplacianPyr

cv2.imshow('original', o)
cv2.imshow('laplacianPyr', laplacianPyr)
cv2.imshow('back', back)

cv2.waitKey()
cv2.destroyAllWindows()
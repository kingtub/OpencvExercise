'''
图像金字塔。（高斯采样）这是向下取样。
'''

import cv2
o = cv2.imread('C:\\D\\testImgs\\' + 'shuqi.jpg')
r1 = cv2.pyrDown(o)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)

cv2.imshow('o', o)
cv2.imshow('r1', r1)
cv2.imshow('r2', r2)
cv2.imshow('r3', r3)

u = r3
for i in range(3):
    u = cv2.pyrUp(u)
cv2.imshow('u', u)

cv2.waitKey()
cv2.destroyAllWindows()

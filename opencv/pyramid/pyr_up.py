'''
图像金字塔。这是（高斯采样）向上取样。
'''

import cv2
o = cv2.imread('C:\\D\\testImgs\\chapter12\\image' + '\\p.bmp')
r1 = cv2.pyrUp(o)
r2 = cv2.pyrUp(r1)
r3 = cv2.pyrUp(r2)

cv2.imshow('o', o)
cv2.imshow('r1', r1)
cv2.imshow('r2', r2)
cv2.imshow('r3', r3)

cv2.waitKey()
cv2.destroyAllWindows()
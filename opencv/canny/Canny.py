'''
Canny 边缘检测
'''

import cv2

o = cv2.imread('C:\\D\\testImgs\\' + 'shuqi.jpg', cv2.IMREAD_GRAYSCALE)
edges1 = cv2.Canny(o, 100, 200)
edges2 = cv2.Canny(o, 64, 128)

cv2.imshow('original', o)
cv2.imshow('edges1', edges1)
cv2.imshow('edges2', edges2)

cv2.waitKey()
cv2.destroyAllWindows()
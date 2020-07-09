''' 把图像中某种颜色的部分提取出来 '''
import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\chapter10\\image\\lenacolor.png')
hsv = cv2.cvtColor(o, cv2.COLOR_BGR2HSV)
low = np.array([100, 20, 46])
up = np.array([150, 255, 255])
mask = cv2.inRange(hsv, low, up)
print(o.shape)
print(mask.shape)
print(np.sum(mask))

c = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

b = cv2.bitwise_and(c[:, :, 0], mask)
g = cv2.bitwise_and(c[:, :, 1], mask)
r = cv2.bitwise_and(c[:, :, 2], mask)
c = cv2.merge([b, g, r])

cv2.imshow('o', o)
cv2.imshow('hsv', hsv)
cv2.imshow('c', c)
cv2.waitKey()
cv2.destroyAllWindows()
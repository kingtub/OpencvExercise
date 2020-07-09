import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\chapter10\\image\\lenacolor.png')
hsv = cv2.cvtColor(o, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist(images=[hsv], channels=[0, 1], mask=None, histSize=[180, 256], ranges=[0, 180, 0, 256])
print(type(hist))
print(o.shape)
print(hsv.shape)
print(hist.shape)

plt.imshow(hist, interpolation='nearest')
plt.show()

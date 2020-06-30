'''
绘制直方图
'''

import cv2
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\chapter14\\image\\boat.bmp')
# 统计各个灰度值
hist = cv2.calcHist(images=[o], channels=[0], mask=None, histSize=[256], ranges=[0, 255])
print(o.shape)
print(type(hist))
print(hist.size)
print(hist.shape)
print(hist)

plt.plot(hist, color='blue')
plt.show()

cv2.imshow('o', o)
cv2.waitKey()
cv2.destroyAllWindows()


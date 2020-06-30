'''
绘制直方图
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\chapter14\\image\\boat.jpg')
print(o.shape)
# 把二维数据转成一维
oneDim = o.ravel()
plt.hist(oneDim, 256)
plt.show()

cv2.imshow('o', o)
cv2.waitKey()
cv2.destroyAllWindows()

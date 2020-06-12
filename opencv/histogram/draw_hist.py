'''
绘制直方图
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\' + 'shuqi.jpg', cv2.IMREAD_GRAYSCALE)
print(o.shape)
# 把二维数据转成一维
oneDim = o.ravel()
plt.hist(oneDim)

cv2.imshow('o', o)
cv2.waitKey()
cv2.destroyAllWindows()

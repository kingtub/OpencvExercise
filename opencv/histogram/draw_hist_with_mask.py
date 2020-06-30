''' 生成掩膜 '''

import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\chapter14\\image\\boat.bmp', cv2.IMREAD_GRAYSCALE)
print(o.shape)
# 掩膜
mask = np.zeros_like(o)
mask[200:400, 200:400] = 255

histMask = cv2.calcHist(images=[o], channels=[0], mask=mask, histSize=[256], ranges=[0, 255])
hist = cv2.calcHist(images=[o], channels=[0], mask=None, histSize=[256], ranges=[0, 255])

plt.plot(histMask, color='red')
plt.plot(hist, color='blue')
plt.show()


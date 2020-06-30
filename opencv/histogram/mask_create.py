''' 生成掩膜 '''

import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\chapter14\\image\\boat.bmp')
# 掩膜
mask = np.zeros_like(o)
mask[200:400, 200:400] = 255
cv2.imshow('ori', o)
cv2.imshow('mask', mask)

# 被掩膜处理过后的图像
masked_img = cv2.bitwise_and(o, mask)
cv2.imshow('masked_img', masked_img)
print(o.shape)
print(mask.shape)

cv2.waitKey()
cv2.destroyAllWindows()

'''
图像形态学只针对二值图像。梯度运算。梯度(image) = 膨胀(image) - 腐蚀(image)
结果是可以得到图像的轮廓(梯度)。
'''

import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\chapter9\\image\\'

o = cv2.imread(img_dir + 'gradient.bmp', cv2.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
r = cv2.morphologyEx(o, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('original', o)
cv2.imshow('result', r)
cv2.waitKey()
cv2.destroyAllWindows()
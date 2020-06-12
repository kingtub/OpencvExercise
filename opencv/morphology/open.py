'''
图像形态学只针对二值图像。开运算，即先对图像腐蚀，再对图像膨胀。
结果是可以对图像（主体结构的外部）去躁, 且保持原图像形状不变。
'''

import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\chapter9\\image\\'

o = cv2.imread(img_dir + 'opening.bmp', cv2.IMREAD_UNCHANGED)
# kernel = np.ones((5, 5), np.uint8)
# Bigger kernel is better
kernel = np.ones((10, 10), np.uint8)
opening = cv2.morphologyEx(o, cv2.MORPH_OPEN, kernel)

cv2.imshow('original', o)
cv2.imshow('opening', opening)

cv2.waitKey()
cv2.destroyAllWindows()
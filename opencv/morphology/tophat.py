'''
图像形态学只针对二值图像。顶帽运算。顶帽(image) = image - 开运算(image)
结果是可以得到图像的噪声部分（例如毛刺）。
'''

import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\chapter9\\image\\'

o = cv2.imread(img_dir + 'tophat.bmp', cv2.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
r = cv2.morphologyEx(o, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('original', o)
cv2.imshow('result', r)
cv2.waitKey()
cv2.destroyAllWindows()
'''
图像形态学只针对二值图像。黑帽运算。黑帽(image) = 闭运算(image) - image
结果是可以得到图像内部的小孔，或前景色中的小黑点
'''

import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\chapter9\\image\\'

o = cv2.imread(img_dir + 'blackhat.bmp', cv2.IMREAD_UNCHANGED)
kernel = np.ones((11, 11), np.uint8)
r = cv2.morphologyEx(o, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('original', o)
cv2.imshow('result', r)
cv2.waitKey()
cv2.destroyAllWindows()
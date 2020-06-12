'''
图像形态学只针对二值图像。这是图像腐蚀。
'''

import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\'

o = cv2.imread(img_dir + 'chapter9\\image\\' + 'erode.bmp', cv2.IMREAD_UNCHANGED)
print(o.shape)
# 卷积核
kernel = np.ones((5, 5), dtype=np.uint8)
result = cv2.erode(o, kernel, iterations=2)
cv2.imshow('original', o)
cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()
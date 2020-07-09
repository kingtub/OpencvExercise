'''alpha 通道'''

import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'aa.jpg')

b, g, r = cv2.split(img)
print(b.shape)
alpha = np.zeros_like(b)
alpha += 255
# 一半的透明度
alpha[300:, :] = 0
merge = cv2.merge([b, g, r, alpha])

cv2.imshow('original', img)
cv2.imshow('new', merge)

cv2.waitKey()
cv2.destroyAllWindows()
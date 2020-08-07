'''alpha 通道'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_dir = 'C:\\D\\testImgs\\chapter12\\image\\'
img = cv2.imread(img_dir + 'lenacolor.png', cv2.IMREAD_UNCHANGED)

b, g, r = cv2.split(img)
print(img.shape)
alpha = np.ones_like(b) * 255
# 一半的透明度
alpha[100:, :] = 128
img_BGRA = cv2.merge([b, g, r, alpha])

cv2.imshow('original', img)
# imshow方法忽略了透明度通道
# cv2.imshow('new', img_BGRA)
plt.imshow(cv2.merge([r, g, b, alpha]))
plt.show()

cv2.imwrite("lena.png", img_BGRA)

cv2.waitKey()
cv2.destroyAllWindows()
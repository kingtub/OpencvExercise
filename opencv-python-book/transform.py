import cv2
import numpy as np


img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'aa.jpg')
kernel = np.array([[0.299, 0.587, 0.114], [- 0.1687, 0.3313, 0.5], [0.5, 0.4187, 0.0813]])
# 就是矩阵相乘：yuv = kernel * img, 针对每一个像素的rgb
yuv = cv2.transform(img, kernel)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', img)
cv2.imshow('y', yuv[:, :, 0])
cv2.imshow('gray', gray)

cv2.waitKey()
cv2.destroyAllWindows()

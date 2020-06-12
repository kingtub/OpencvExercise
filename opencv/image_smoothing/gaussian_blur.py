'''
图像平滑-高斯滤波
'''

import cv2
img_dir = 'C:\\D\\testImgs\\'

imageNoise = cv2.imread(img_dir + 'chapter8\\image\\' + 'lenaNoise.png')
# 均值滤波
resultBlur = cv2.blur(imageNoise, (5, 5))
resultGaussianBlur = cv2.GaussianBlur(imageNoise, (5, 5), sigmaX=0)
cv2.imshow('original', imageNoise)
cv2.imshow('blur', resultBlur)
cv2.imshow('gaussian_blur', resultGaussianBlur)
cv2.waitKey()
cv2.destroyAllWindows()
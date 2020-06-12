'''
图像平滑-中值滤波
'''

import cv2
img_dir = 'C:\\D\\testImgs\\'

imageNoise = cv2.imread(img_dir + 'chapter8\\image\\' + 'lenaNoise.png')
# 均值滤波
resultBlur = cv2.blur(imageNoise, (5, 5))
# 高斯滤波
resultGaussianBlur = cv2.GaussianBlur(imageNoise, (5, 5), sigmaX=0)
# 中值滤波，比前面几种效果更好
resultMedian = cv2.medianBlur(imageNoise, 5)
cv2.imshow('original', imageNoise)
cv2.imshow('blur', resultBlur)
cv2.imshow('gaussian_blur', resultGaussianBlur)
cv2.imshow('median_blur', resultMedian)
cv2.waitKey()
cv2.destroyAllWindows()
'''
图像平滑-均值滤波
'''

import cv2
img_dir = 'C:\\D\\testImgs\\'

imageNoise = cv2.imread(img_dir + 'chapter8\\image\\' + 'lenaNoise.png')
result = cv2.blur(imageNoise, (5, 5))
result2 = cv2.blur(imageNoise, (10, 10))
cv2.imshow('original', imageNoise)
cv2.imshow('result', result)
cv2.imshow('result2', result2)
cv2.waitKey()
cv2.destroyAllWindows()
'''
通道的拆分与合并
'''
import cv2
import numpy as np
img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'shuqi.jpg')
b, g, r = cv2.split(img) # 拆分通道
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
merge = cv2.merge([b, g, r]) # 合并通道
cv2.imshow('merge', merge)
#cv2.imshow('merge2', cv2.merge([r, g, b])) # wrong, 蓝精灵。通道反了

rows, cols, chanels = img.shape
aZeros = np.zeros((rows, cols, 1), dtype=img.dtype)
cv2.imshow('Only_Blue',cv2.merge([b, aZeros, aZeros]))
cv2.imshow('Only_Red',cv2.merge([aZeros, aZeros, r]))
cv2.imshow('Only_Green',cv2.merge([aZeros, g, aZeros]))

cv2.waitKey()
cv2.destroyAllWindows()
import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'shuqi.jpg')
blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

merge = np.zeros_like(img)
merge[:, :, 0] = blue
merge[:, :, 1] = green
merge[:, :, 2] = red

cv2.imshow('original', img)
cv2.imshow('merge', merge)

cv2.waitKey()
cv2.destroyAllWindows()
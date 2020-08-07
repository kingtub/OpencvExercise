''' 画个矩形 '''
import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'aa.jpg')

cv2.rectangle(img, (100, 100), (200, 200), color=(0, 255, 0), thickness=2)
cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()
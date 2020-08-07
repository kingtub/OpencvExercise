''' 画一条线 '''
import cv2
import numpy as np

createdImg = np.zeros((512, 512, 3), np.uint8)
cv2.line(createdImg, (0, 0), (511, 511), color=(0, 0, 255), thickness=5)
cv2.imshow('createdImg', createdImg)

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'aa.jpg')
cv2.line(img, (0, 0), (img.shape[0] - 1, img.shape[1] - 1), color=(0, 255, 0), thickness=5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

cv2.circle(img, (200, 300), 50, (0, 0, 255), 1)
cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()
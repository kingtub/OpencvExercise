'''
图像缩放
'''
import cv2

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'shuqi.jpg')
result = cv2.resize(img, dsize=None, fx=2, fy=1)
cv2.imshow('ori', img)
cv2.imshow('resize', result)
cv2.waitKey()
cv2.destroyAllWindows()
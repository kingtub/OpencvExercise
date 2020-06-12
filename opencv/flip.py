'''
图像翻转
'''
import cv2
img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'shuqi.jpg')

# flipCode只有3种可能，0：上下翻转，即以y轴为对称轴翻转；
# 大于0：左右翻转，即以x轴为对称轴翻转
# 小于0：先以x轴翻转，再以y轴翻转

x = cv2.flip(img, 0)
y = cv2.flip(img, 1)
xy = cv2.flip(img, -1)
cv2.imshow('original', img)
cv2.imshow('x', x)
cv2.imshow('y', y)
cv2.imshow('xy', xy)
cv2.waitKey()
cv2.destroyAllWindows()
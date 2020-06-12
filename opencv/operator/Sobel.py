
import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\chapter10\\image\\'

def sobelIt(image_path):
    o = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 用 CV_64F 防止数字溢出
    sobelX = cv2.Sobel(o, cv2.CV_64F, True, False)
    # 再转成 np.uint8
    sobelX = cv2.convertScaleAbs(sobelX)

    sobelY = cv2.Sobel(o, cv2.CV_64F, False, True)
    sobelY = cv2.convertScaleAbs(sobelY)

    # 相加得到XY边界都显示的
    sobelXY = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)

    cv2.imshow('original', o)
    cv2.imshow('sobelX', sobelX)
    cv2.imshow('sobelY', sobelY)
    cv2.imshow('sobelXY', sobelXY)

    cv2.waitKey()
    cv2.destroyAllWindows()


sobelIt(img_dir + 'sobel.bmp')
sobelIt('C:\\D\\testImgs\\' + 'shuqi.jpg')
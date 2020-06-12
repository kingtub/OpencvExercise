'''
拉普拉斯 算子
'''
import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\chapter10\\image\\'

def doIt(image_path):
    o = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 用 CV_64F 防止数字溢出
    sobelX = cv2.Sobel(o, cv2.CV_64F, True, False)
    # 再转成 np.uint8
    sobelX = cv2.convertScaleAbs(sobelX)
    sobelY = cv2.Sobel(o, cv2.CV_64F, False, True)
    sobelY = cv2.convertScaleAbs(sobelY)

    # 相加得到XY边界都显示的
    sobelXY = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)

    # 用 CV_64F 防止数字溢出
    scharrX = cv2.Scharr(o, cv2.CV_64F, True, False)
    # 再转成 np.uint8
    scharrX = cv2.convertScaleAbs(scharrX)
    scharrY = cv2.Scharr(o, cv2.CV_64F, False, True)
    scharrY = cv2.convertScaleAbs(scharrY)

    scharrXY = cv2.addWeighted(scharrX, 0.5, scharrY, 0.5, 0)

    laplacianImg = cv2.Laplacian(o, cv2.CV_64F)
    laplacianImg = cv2.convertScaleAbs(laplacianImg)
    cv2.imshow('original', o)
    cv2.imshow('sobelXY', sobelXY)
    cv2.imshow('scharrXY', scharrXY)
    cv2.imshow('laplacian', laplacianImg)

    cv2.waitKey()
    cv2.destroyAllWindows()


doIt(img_dir + 'scharr.bmp')
doIt('C:\\D\\testImgs\\' + 'shuqi.jpg')
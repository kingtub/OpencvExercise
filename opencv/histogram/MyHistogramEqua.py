'''  直方图均衡化  '''
import numpy as np
import cv2


# 限定输入img必须是灰度图像
def HistogramEqua(img):
    result = np.zeros_like(img)
    hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0, 255])
    histP = hist / (img.shape[0] * img.shape[1])
    histP = histP.cumsum(axis=0)
    histP = histP * 255
    histP = np.round(histP)
    map = histP.astype(np.uint8)
    m, n = img.shape
    for i in range(m):
        for j in range(n):
            result[i, j] = map[img[i, j], 0]

    return result


def my_use():
    o = cv2.imread('C:\\D\\testImgs\\chapter14\\image\\equ.bmp', cv2.IMREAD_GRAYSCALE)
    r = HistogramEqua(o)

    o2 = cv2.imread('C:\\D\\testImgs\\chapter14\\image\\equ2.bmp', cv2.IMREAD_GRAYSCALE)
    r2 = HistogramEqua(o2)

    cv2.imshow('o', o)
    cv2.imshow('r', r)

    cv2.imshow('o2', o2)
    cv2.imshow('r2', r2)

    cv2.waitKey()
    cv2.destroyAllWindows()


# my_use()
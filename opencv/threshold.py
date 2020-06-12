'''
阈值化
'''

import cv2
img_dir = 'C:\\D\\testImgs\\'


def thresh():
    img = cv2.imread(img_dir + 'shuqi_gray.bmp', cv2.IMREAD_UNCHANGED)
    # 二值化，把大于阈值的像素置为255，小于等于阈值的像素置为0
    ret, binaryImg = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    # 二值化反，和THRESH_BINARY相反，把大于阈值的像素置为0，小于等于阈值的像素置为255
    ret2, binaryInvImg = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    # 截断阈值化，把大于阈值的像素置为阈值，小于等于阈值的像素不变
    ret3, truncImg = cv2.threshold(img, 128, 255, cv2.THRESH_TRUNC)
    # 阈值化为0，把大于阈值的像素不变，小于等于阈值的像素为0
    ret4, toZero = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)
    # 反阈值化为0，把大于阈值的像素置为0，小于等于阈值的像素不变
    ret5, toZeroInv = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('original', img)
    cv2.imshow('dst', binaryImg)
    cv2.imshow('dstInv', binaryInvImg)
    cv2.imshow('trunc', truncImg)
    cv2.imshow('toZero', toZero)
    cv2.imshow('toZeroInv', toZeroInv)
    cv2.waitKey()
    cv2.destroyAllWindows()




thresh()
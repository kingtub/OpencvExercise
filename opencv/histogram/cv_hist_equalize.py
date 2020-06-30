import cv2
import MyHistogramEqua
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\chapter14\\image\\equ.bmp', cv2.IMREAD_GRAYSCALE)
o2 = cv2.imread('C:\\D\\testImgs\\chapter14\\image\\equ2.bmp', cv2.IMREAD_GRAYSCALE)

r11 = MyHistogramEqua.HistogramEqua(o)
r12 = MyHistogramEqua.HistogramEqua(o2)

r21 = cv2.equalizeHist(o)
r22 = cv2.equalizeHist(o2)

cv2.imshow('o', o)
cv2.imshow('r11', r11)
cv2.imshow('r12', r12)

cv2.imshow('o2', o2)
cv2.imshow('r21', r21)
cv2.imshow('r22', r22)

cv2.waitKey()
cv2.destroyAllWindows()

#灰度直方图比较
plt.hist(o.ravel(), 256)
plt.figure()
plt.hist(r11.ravel(), 256)
plt.figure()
plt.hist(r21.ravel(), 256)
plt.show()
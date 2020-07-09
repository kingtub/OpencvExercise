import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('C:\\D\\testImgs\\chapter10\\image\\lenacolor.png')
hsv = cv2.cvtColor(o, cv2.COLOR_BGR2HSV)
hist, xbins, ybins = np.histogram2d(hsv[:, :, 0].ravel(), hsv[:, :, 1].ravel(), [180, 256], [[0, 180], [0, 256]])


cv2.imshow('o', o)
cv2.waitKey()
cv2.destroyAllWindows()
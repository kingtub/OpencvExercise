import cv2
import numpy as np

def test_filter2D():
    img_dir = 'C:\\D\\testImgs\\'

    imageNoise = cv2.imread(img_dir + 'chapter8\\image\\' + 'lenaNoise.png')
    blur = cv2.blur(imageNoise, (5, 5))
    cv2.imshow('original', imageNoise)
    cv2.imshow('blur', blur)

    kernel = np.ones((5, 5), np.float32) / 25
    filter2dImg = cv2.filter2D(imageNoise, -1, kernel)
    cv2.imshow('filter2dImg', filter2dImg)

    cv2.waitKey()
    cv2.destroyAllWindows()


test_filter2D()
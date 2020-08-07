import cv2
import numpy as np

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'aa.jpg')

face_detect1 = cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')
faces1 = face_detect1.detectMultiScale(img)
print('faces1:', faces1)
for (x, y, width, height) in faces1:
    cv2.rectangle(img, (x, y), (x + width, y + height), color=(0, 255, 0), thickness=2)

face_detect2 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces2 = face_detect2.detectMultiScale(img)
print('faces2:', faces2)
for (x, y, w, h) in faces2:
    color = (0, 0, 255)
    cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    # 左眼
    cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
               color)
    # 右眼
    cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
               color)
    # 嘴巴
    cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                  (x + 5 * w // 8, y + 7 * h // 8), color)

cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()

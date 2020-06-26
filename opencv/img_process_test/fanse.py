''' 实现反色 '''
import cv2

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'shuqi.jpg')
cv2.imshow("original", img)

print(type(img))
print(img.shape)

revert = 255 - img
cv2.imshow('revert', revert)

print(img[0:1, :5, :2])
print(revert[0:1, :5, :2])

cv2.waitKey()  # 让显示图片窗口等待，否则一闪而过。这个方法是阻塞的
cv2.destroyAllWindows() # 毁掉所有窗口，类似清空内存
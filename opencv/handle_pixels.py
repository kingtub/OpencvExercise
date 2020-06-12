import cv2

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'shuqi.jpg')
cv2.imshow("original", img)

img[300:, 0:200] = [0, 255, 0] #操作多个像素，修改左下角部分；灰度图只有一个颜色通道，彩图有3个通道，B、G、R顺序
# 当然可以只操作一个像素
# img[100, 120] = [255, 255, 255]
cv2.imshow("changed", img)

cv2.waitKey()  # 让显示图片窗口等待，否则一闪而过。这个方法是阻塞的
cv2.destroyAllWindows() # 毁掉所有窗口，类似清空内存
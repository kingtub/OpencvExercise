import cv2

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + 'aa.jpg')
cv2.imshow("aa", img)
cv2.waitKey()  # 让显示图片窗口等待，否则一闪而过。这个方法是阻塞的
cv2.destroyAllWindows() # 毁掉所有窗口，类似清空内存
cv2.imwrite(img_dir + "bb.jpg", img)  # 复制文件
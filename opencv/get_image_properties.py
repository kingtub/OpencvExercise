import cv2

img_dir = 'C:\\D\\testImgs\\'
img = cv2.imread(img_dir + "shuqi.jpg")
print(img.shape) # print (468, 500, 3) ,代表像素行数、列数、颜色通道数；若是灰度图，因为只有一个通道，所以只有行数、列数
print(img.size) # print 702000 = 468 * 500 * 3; 若是灰度图，那么等于468 * 500
print(img.dtype) # print uint8 每个像素的数据类型
import cv2
img_dir = 'C:\\D\\testImgs\\'

def bgr2gray():
    img = cv2.imread(img_dir + 'shuqi.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    cv2.imwrite(img_dir + 'shuqi_gray.jpg', gray)
    print(img.shape)
    print(gray.shape)
    cv2.waitKey()
    cv2.destroyAllWindows()


def gray2bgr():
    img = cv2.imread(img_dir + 'shuqi_gray.jpg', cv2.IMREAD_UNCHANGED)
    bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.imshow('bgr', bgr)
    b, g, r = cv2.split(bgr)
    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    cv2.imshow('red', r)
    print(bgr.shape)
    cv2.waitKey()
    cv2.destroyAllWindows()

def bgr2rgb():
    img = cv2.imread(img_dir + 'shuqi.jpg')
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('bgr', img)
    cv2.imshow('rgb', rgb)
    cv2.waitKey()
    cv2.destroyAllWindows()


bgr2gray()
# gray2bgr()
#bgr2rgb()
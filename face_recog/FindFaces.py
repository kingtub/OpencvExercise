import face_recognition
import cv2

img_dir = 'C:\\D\\testImgs\\'
# img = cv2.imread(img_dir + 'aa.jpg')
image = face_recognition.load_image_file(img_dir + 'aa.jpg')

#  The coordinates reported are the top, right, bottom and left coordinates of the face (in pixels)
face_locations = face_recognition.face_locations(image)

print(type(image))
print(type(face_locations))
print(face_locations)

cvImg = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
pt1 = (face_locations[0][3], face_locations[0][0])
pt2 = (face_locations[0][1], face_locations[0][2])
cv2.rectangle(cvImg, pt1, pt2, (0, 255, 0), thickness=2)
# cv2.imshow("i", image)
cv2.imshow("cvImg", cvImg)

img_names = ['shuqi_feng.jpg', 'mul-people.jpg']
for ss in img_names:
    img2 = face_recognition.load_image_file(img_dir + ss)
    face_locations2 = face_recognition.face_locations(img2)
    cvImg2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
    for loc in face_locations2:
        ptlt = (loc[3], loc[0])
        ptbr = (loc[1], loc[2])
        cv2.rectangle(cvImg2, ptlt, ptbr, (0, 255, 0), thickness=2)
    cv2.imshow(ss, cvImg2)

cv2.waitKey()
cv2.destroyAllWindows()


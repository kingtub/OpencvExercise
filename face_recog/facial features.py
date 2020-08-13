import face_recognition
import cv2

img_dir = 'C:\\D\\testImgs\\'
image = face_recognition.load_image_file(img_dir + 'aa.jpg')
face_landmarks_list = face_recognition.face_landmarks(image)
imgCv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

print(type(face_landmarks_list))
print(face_landmarks_list)

for face in face_landmarks_list:
    for k in face.keys():
        pts = face[k]
        for i in range(len(pts) - 1):
            cv2.line(imgCv, pts[i], pts[i+1], (255, 255, 255), thickness=1)

cv2.imshow("img", imgCv)
cv2.waitKey()
cv2.destroyAllWindows()

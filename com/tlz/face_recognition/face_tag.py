import cv2
import face_recognition

'''
https://zhuanlan.zhihu.com/p/32961280

'''

# 首先我们定义了标签集，存在names数组中。标签名字也是我们图片的文件名。
names = [
    "zm1",
    "txq",
    "catherine",
    "william",
]

images = []
for name in names:
    filename = name + ".jpg"
    # 调用face_recognition.load_image_file从图片中读取数据。
    image = face_recognition.load_image_file(filename)
    images.append(image)
unknown_image = face_recognition.load_image_file("w4.jpg")

face_encodings = []
for image in images:
    encoding = face_recognition.face_encodings(image)[0]
    face_encodings.append(encoding)
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

face_locations = face_recognition.face_locations(unknown_image)
for i in range(len(unknown_face_encodings)):
    unknown_encoding = unknown_face_encodings[i]
    face_location = face_locations[i]
    top, right, bottom, left = face_location
    cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)
    results = face_recognition.compare_faces(face_encodings, unknown_encoding)
    for j in range(len(results)):
        if results[j]:
            name = names[j]
            cv2.putText(unknown_image, name, (left - 10, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

unknown_image_rgb = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
cv2.imshow("Output", unknown_image_rgb)
cv2.waitKey(0)

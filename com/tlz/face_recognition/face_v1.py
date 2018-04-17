# -*- coding: utf-8 -*-
#

'''

也可以使用PIL包

PIL 是基本的图像处理的包

opencv 很强悍的图像处理的
cv2  opencv-python 包

wh.jpg  识别识别 原始图 大
wh.png  成功！

'''

# 检测人脸
import face_recognition
import cv2

img_path = 'wh.png'
# 读取图片并识别人脸
img = face_recognition.load_image_file(img_path)
face_locations = face_recognition.face_locations(img)
print('识别到 {} 张人脸'.format(len(face_locations)))


# 调用opencv函数显示原图
# img = cv2.imread("2.jpg")
# cv2.namedWindow("原图")
# cv2.imshow("原图", img)

# 遍历每个人脸，并标注
faceNum = len(face_locations)
for i in range(0, faceNum):
    top = face_locations[i][0]
    right = face_locations[i][1]
    bottom = face_locations[i][2]
    left = face_locations[i][3]

    # 左上角 坐标起点||
    start = (left, top)
    end = (right, bottom)

    color = (55, 255, 155)  # 标记框的颜色rgb
    thickness = 3
    cv2.rectangle(img, start, end, color, thickness)

# 显示识别结果
cv2.namedWindow("识别")
cv2.imshow("识别", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

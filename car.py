# car.py
import cv2
import numpy as np
import keyboard

img_path = 'car_number.jpg'
ori_img = cv2.imread("D:/opencv/car_number.JPG", cv2.imread(img_path))

src = [] # 왼쪽위, 오른쪽위, 오른쪽아래, 왼쪽아래 순으로 각 점의 좌표
import mouse_handler




# 32비트로 바꿔줌
src_np = np.array(src, dtype=np.float32)

# width ,height 길이 계산
width = max(np.linalg.norm(src_np[0] - src_np[1]), np.linalg.norm(src_np[2] - src_np[3]))
height = max(np.linalg.norm(src_np[0] - src_np[3]), np.linalg.norm(src_np[1] - src_np[2]))

# width, height 비율
width_ratio = (width / height)
height_ratio = 1

# 비율 * 300 으로 픽셀 크기 맞춤
dst_np = np.array([[0, 0],
        [int(width_ratio * 300), 0],
        [int(width_ratio * 300), int(height_ratio * 300)],
        [0, int(height_ratio * 300)]
        ], dtype=np.float32)

M = cv2.getPerspectiveTransform(src=src_np, dst=dst_np)
result = cv2.warpPerspective(ori_img, M=M, dsize=(int(width_ratio * 300), height_ratio * 300))
#print("Perspective Transformation :\n", M)

cv2.imshow('img', ori_img)

print("스페이스바를 누르면 번호판의 4개 매칭점이 구해집니다.")

if cv2.waitKey(0) == ord(' '):
   for xx, yy in src:
     cv2.circle(ori_img, center=(xx, yy), radius=5, color=(0, 255, 0), thickness=-1, lineType=cv2.LINE_AA)
cv2.imshow('img', ori_img)
print("original points : \n", src_np)

if cv2.waitKey(0) == ord(' '):
   cv2.imshow('result', result)
   print("\ndestination points : \n", dst_np)

if cv2.waitKey(0) == ord(' '):
   cv2.destroyAllWindows()


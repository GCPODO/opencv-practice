# mouse_handler.py
import cv2
import nu

img_path = 'car_number.jpg'
ori_img = cv2.imread("D:/opencv/car_number.JPG", cv2.imread(img_path))

src = [] # 왼쪽위, 오른쪽위, 오른쪽아래, 왼쪽아래 순으로 각 점의 좌표

# mouse callback handler
def mouse_handler(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONUP: # 마우스가 좌클릭을 했을때 (4번의 클릭으로 좌표 얻기)
     img = ori_img.copy()

     src.append([x, y])

     for xx, yy in src: # 클릭한 곳에 점 그리기
        cv2.circle(img, center=(xx, yy), radius=5, color=(0, 255, 0), thickness=-1)

     cv2.imshow('Original Image - Car', img)

     # perspective transform
     if len(src) == 4:
        src_np = np.array(src, dtype=np.float32)
        print("original points : \n", src_np)

cv2.namedWindow('Original Image - Car')
cv2.setMouseCallback('Original Image - Car', mouse_handler) # 마우스 이벤트 전달

cv2.imshow('Original Image - Car', ori_img)
if cv2.waitKey(0) == 32:
   cv2.destroyAllWindows()



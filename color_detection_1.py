##### 실행 #####
# sudo python3 color_detection_image.py --image 이미지 경로
# 예) sudo python3 color_detection_image.py --image test.jpg

# 필요한 패키지 import
import numpy as np  # 파이썬 행렬 수식 및 수치 계산 처리 모듈
import argparse  # 명령행 파싱(인자를 입력 받고 파싱, 예외처리 등) 모듈
import cv2  # opencv 모듈

# 실행을 할 때 인자값 추가
ap = argparse.ArgumentParser()
# 입력받을 인자값 등록
ap.add_argument("-i", "--image", required=True, help="이미지 경로")
# 입력받은 인자값을 args에 저장
args = vars(ap.parse_args())

# input 이미지 읽기
image = cv2.imread(args["/D:/opencv/traffic_light.jpg"])

# 검출할 색상 목록(색의 가까운 수의 범위(배열)이 저장된 튜플)
colors = [
    ([200, 200, 200], [255, 255, 255]),  # 흰색
    ([0, 0, 150], [100, 100, 255]),  # 빨간색
    ([0, 150, 0], [100, 255, 100]),  # 초록색
    ([150, 0, 0], [255, 100, 100]),  # 파란색
    ([150, 150, 0], [255, 255, 100]),  # 하늘색
    ([150, 0, 150], [255, 100, 255]),  # 보라색
    ([0, 150, 150], [100, 255, 255])  # 노란색
]

# 검출 결과를 저장할 배열
result = []

# 검출할 색상 목록(colors)의 길이만큼 반복
for (low, high) in colors:
    # low와 high 배열을 numpy 배열 및 부호 없는 정수의 데이터 타입(dtype="uint8")으로 변환([0, 0, 0] -> [0 0 0])
    low = np.array(low, dtype="uint8")  # 검출할 색상의 범위에서 최솟값
    high = np.array(high, dtype="uint8")  # 검출할 색상의 범위에서 최댓값

    # cv2.inRange(image, low, high) : 이미지에서 low와 high 사이 범위의 색상을 검출
    # - image : 검출할 이미지
    # - low : 검출할 색상의 최솟값
    # - high : 검출할 색상의 최댓값
    mask = cv2.inRange(image, low, high)

    # cv2.bitwise_and(image1, image2, mask) : image1과 image2를 AND 연산(이미지 비트 연산)을 통해 mask 영역만 추출
    # - mask : 검출할 영역(mask를 제외한 영역은 검정색)
    detection = cv2.bitwise_and(image, image, mask=mask)

    # 검출한 이미지를 result 배열에 저장
    result.append(detection)  # append : 배열의 원소 추가

# 이미지 show
cv2.imshow("/D:/opencv/traffic_light.jpg", image)  # 원본 이미지

number = 0

# 검출 결과인 result 배열의 길이만큼 반복
for detection in result:
    number += 1

    # 이미지 show
    cv2.imshow("result%d" % number, detection)  # 색상을 검출한 결과 이미지

# 입력 무한 대기
cv2.waitKey(0)
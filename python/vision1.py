import cv2
import numpy as np

# 이미지 불러오기
img_1 = cv2.imread("D:\\kmu_vision\\image\\512test1star.bmp")
img_2 = cv2.imread("D:\\kmu_vision\\image\\butterfly.bmp")
img_3 = cv2.imread("D:\\kmu_vision\\image\\camera.bmp")

# 이미지 출력
cv2.imshow('Image1',img_1) # 앞에 이미지 이름을 넣어 주지 않으면 실행 안됨
cv2.imshow('Image2',img_2)
cv2.imshow('Image3',img_3)
cv2.waitKey() # 키입력 대기 함수 (사용하지 않을 경우, 윈도우 창이 유지되지 않고 프로그램이 종료 됨)
cv2.destroyAllWindows() # 키 입력시 모든 윈도우 창 제거

# 픽셀값 확인
print(np.shape(img_1)) # open cv에서 다루는 영상은 numpy가 제공하는 다양한 기능(함수) 사용가능
print(np.shape(img_2))
print(np.shape(img_3))
print(img_1[0,0,0], img_1[0,0,1], img_1[0,0,2]) # (0,0) 화소 조사

# 사이즈 확인
print(img_1.size) # 512 * 512 * 3 = 786432 , 786432로 출력 됨
print(img_2.size) # 512 * 512 * 3 = 786432 , 786432로 출력 됨
print(img_3.size) # 512 * 512 * 3 = 786432 , 786432로 출력 됨

gray2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY) # 명암 영상으로 변환
print(np.shape(gray2)) # 2차원 배열
gray2_small = cv2.resize(gray2, dsize=(0,0), fx = 0.5, fy = 0.5) # 반으로 축소
cv2.imshow('grayimage2',gray2)
cv2.imshow('gray_small image', gray2_small)
cv2.waitKey()
cv2.destroyAllWindows()


cv2.rectangle(img_2, (100,100), (200,200), (0,0,255),2)
# cv2.putText(img,)
cv2.putText(img_2, 'hello', (100,90),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv2.imshow('test1',img_2)
cv2.waitKey()
cv2.destroyAllWindows()
print('hello')
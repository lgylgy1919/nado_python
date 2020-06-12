from random import *

print(random())  # 0.0 ~ 1.0미만의 임의 값 생성
print(random() * 10)  # 0.3~10.0미만의 임의 값 생성
print(int(random()*10))  # 0~10미만의 임의 정수 생성
print(int(random()*10))  # 0~10미만의 임의 정수 생성
print(int(random()*10))  # 0~10미만의 임의 정수 생성
print(int(random()*10) + 1)  # 1~10이하의 임의 정수 생성
print(int(random()*10) + 1)  # 1~10이하의 임의 정수 생성
print(int(random()*10) + 1)  # 1~10이하의 임의 정수 생성

print(int(random()*45)+1)  # 1부터 45이하의 임의 정수 생성

print(randrange(1, 46))  # 1부터  46미만의 임의 정수 생성
print(randint(1, 45))  # 1부터 45이하의 임의 정수 생성


offline = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", offline, "일로 선정되었습니다.")

'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을받게 됩니다.
추첨 프로그램을 작성하시오

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다. --
'''
# 일단 20명 중 4명 뽑기
# 그 4명 중 1명 뽑기
from random import *
id_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
four = sample(id_, 4)
one = four[0]
three = four[1:]

print(f"--당첨자 발표\n치킨 당첨자:{one}\n커피 당첨자:{three}\n--축하합니다.--")


# 유튜브 풀이
users = range(1, 21)  # 1부터 20까지의 숫자 생성, 단 type이 range
users = list(users)  # range 타입을 list로 변경

shuffle(users)  # 1부터 20의 숫자를 무작위로 재배열
winners = sample(users, 4)


print(" -- 당첨자 발표 --")
print(" 치킨 당첨자 : {0}".format(winners[0]))
print(" 커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하 합니다 --")

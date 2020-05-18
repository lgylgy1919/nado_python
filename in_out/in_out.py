# import sys
# print("Python", "Java", "JavaScript", sep=" vs ")
# print("Python", "Java", end="? ")
# print("무엇이 더 재미있을까요?")

# '''
# Python vs Java vs JavaScript
# Python Java?무엇이 더 재미있을까요?
# '''

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학": 0, "영어": 50, "코딩": 10}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 21):
#     # print("대기번호 : " + str(num))
#     print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이 입력하세요 : ")  # 어떤 값이든 문자열로 출력
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

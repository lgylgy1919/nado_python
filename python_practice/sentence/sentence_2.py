# 슬라이싱
jumin = "990120-1234567"

print("성별:"+jumin[7])
print("연:" + jumin[0:2])  # 0번째부터 2번쨰 직전까지
print("월:" + jumin[2:4])
print("일:" + jumin[4:6])

print("생년월일: " + jumin[:6])  # 처음부터 6번째 직전까지
print("뒤 일곱자리:" + jumin[7:14])
print("뒤 일곱자리:" + jumin[7:])  # 7부터 끝까지
print("뒤 7자리(뒤에부터):" + jumin[-7:14])  # 뒤 7번째 자리부터
print("뒤 7자리(뒤에부터):" + jumin[-7:])

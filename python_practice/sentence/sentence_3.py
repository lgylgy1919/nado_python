python = "Python is Amazing"
print(python.lower())  # 문자열을 소문자로 출력
print(python.upper())  # 문자열을 대문자로 출력
print(python[0].isupper())  # 문자열의 첫 번째 값이 대문자인가? True
print(len(python))  # 문자열의 길이 : 17
print(python.replace("Python", 'Java'))  # Java is Amazing

index = python.index("n")  # 처음 n이 나온 위치 찾는다.
print(index)  # 5
index = python.index("n", index+1)  # n이 나온 위치 다음부터 n을 찾는다.
print(index)  # 15

print(python.find("n"))  # 처음 n이 나온 위치 찾는다.
print(python.find("java"))  # 없는 값은 -1이 출력된다.
print(python.count("n"))  # n이 총 몇번 나오는가.
print(python.index("java"))  # 없는 값은 오류

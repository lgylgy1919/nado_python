print("a"+"b")
print("a", "b")

# 방법1
print("나는 %d살입니다." % 20)  # d는 정수값.
print("나는 %s를 좋아해요." % "파이썬")  # s는 문자열.
print("Apple 은 %c로 시작해요." % "A")  # c는 문자.


# %s로 하면 정수, 문자열, 문자 모두 가능
print("나는 %s살입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple 은 %s로 시작해요." % "A")

# 한 개 이상의 값, 순서대로 들어간다.
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

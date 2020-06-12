# 집합(set)
# 중복이 안되고, 순서가 없다.
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}

java = {"유재석", "김태호", "양세형 "}
python = set(["유재석", "박명수"])

# 자바와 파이썬 교집합
print(java & python)  # {'유재석'}
print(java.intersection(python))  # {'유재석'}

# 자바와 파이썬 합집합
print(java | python)  # {'박명수', '김태호', '유재석', '양세형 '}
print(java.union(python))  # {'박명수', '김태호', '유재석', '양세형 '}


# 자바는 할 수 있지만 파이썬은 할 수 없는 개발자 (차집합)
print(java - python)  # {'양세형 ', '김태호'}
print(java.difference(python))  # {'양세형 ', '김태호'}

# 파이썬 할 수 있는 사람 늘어난 경우
python.add("김태호")
print(python)  # {'유재석', '김태호', '박명수'}

# 자바를 까먹은 경우
python.remove("김태호")
print(python) #{'유재석', '박명수'}

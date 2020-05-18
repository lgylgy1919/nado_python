subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]  # [10, 20, 30]

subway = ["유재석", " 박명수", "조세호"]

# 몇 번째에 있는가
index_ = subway.index("조세호")
print(index_)  # 2

# 뒤에 추가하기
subway.append("하하")
print(subway)  # ['유재석', ' 박명수', '조세호', '하하']

# n번째에 추가하기
subway.insert(1, "정형돈")
print(subway)  # ['유재석', '정형돈', ' 박명수', '조세호', '하하']

# 뒤에서 꺼내기
pop_ = subway.pop()
print(pop_)   # "하하"
print(subway)  # ['유재석', '정형돈', ' 박명수', '조세호']

# 같은 이름의 사람이 몇 명 있는지 확인하기
bus = ["유재석", "하하", "박명수", "유재석"]
count = bus.count("유재석")
print(count)

# 순서대로 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
# 순서 뒤집기
num_list.reverse()
print(num_list)
# 모두 지우기
num_list.clear()
print(num_list)

# 자료형에 구애받지 않고 다양한 객체 사용 가능
mix_list = ["조세호", True, 5]
print(mix_list)

# 리스트 확장
color = ["red", "blue", "green"]
shape = ["circle", "triangle", "square"]
color.extend(shape)  # color 리스트에 shpae리스트를 붙여 넣는 것
print(color)

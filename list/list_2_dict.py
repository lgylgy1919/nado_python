cabinet = {3: "유재석", 100: "이재윤"}
print(cabinet[3])  # 유재석
print(cabinet[100])  # 이재윤

print(cabinet.get(3))  # 유재석
print(cabinet.get(5))  # None
print(cabinet.get(5, "사용 가능"))  # 5에 해당하는 VALUE가 있으면 VALUE값 출력, 없으면 사용가능 출력
# print(cabinet[5])  # ERROR

print(3 in cabinet)  # True


drawer = {"A-3": "박명수", "B-3": "노홍철"}
print(drawer["A-3"])  # 박명수
print(drawer.get("B-3"))  # 노홍철

# 추가
drawer["C-3"] = "조세호"
print(drawer)  # {'A-3': '박명수', 'B-3': '노홍철', 'C-3': '조세호'}
drawer["A-3"] = "김종국"
print(drawer)  # {'A-3': '김종국', 'B-3': '노홍철', 'C-3': '조세호'}


# 삭제
del drawer["A-3"]
print(drawer)  # {'B-3': '노홍철', 'C-3': '조세호'}

# key값만 출력
print(drawer.keys())  # dict_keys(['B-3', 'C-3'])

# value값만 출력
print(drawer.values())  # dict_values(['노홍철', '조세호'])

# key-value
print(drawer.items())  # dict_items([('B-3', '노홍철'), ('C-3', '조세호')])

#  dict 삭제
drawer.clear()
print(drawer)  # {}

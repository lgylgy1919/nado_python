'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

예) http: // naver.com
규칙1.  http:// 부분은 제외=> naver.com
규칙2. 처음 만나는 점(.) 이후 부분은 제외= > naver
규칙3. 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

예) 생성된 비밀번호: nav51!
'''
homepage = "http://google.com"

index_1 = homepage.index("/") + 2
rule_1 = homepage[index_1:]  # google.com
index_2 = rule_1.index(".")
rule_2 = rule_1[:index_2]  # google

count_1 = rule_2[:3]  # goo
count_2 = len(rule_2)  # 6
count_3 = rule_2.count("e")
password = count_1 + str(count_2) + str(count_3) + "!"

print(password)

url = "http://naver.com"

my_str = url.replace("http://", "")  # 규칙1
my_str = my_str[:my_str.index(".")]  # 규칙2
password_ = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1}입니다.".format(url, password_))

'''
회의가 가장 빨리 끝나는 순서
그 다음 시작하는 회의 중 가장 빨리 끝나는 회의

'''
# 리스트 만들기
# 두 번째 인자 오름차순으로 정렬
# 
n = int(input())
lists = []
for i in range(n):
    a = list(map(int,input().split(" ")))
    lists.append(a)

assign = []
lists.sort(key=lambda x:x[1])
assign.append(lists[0])

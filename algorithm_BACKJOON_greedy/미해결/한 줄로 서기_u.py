'''
4
2 1 1 0
---
4 2 1 3
'''
from itertools import permutations

n = int(input())
h = list(map(int,input().split(" ")))
lists = []
for i in range(n):
    lists.append(i+1)
kindOfLine = list(permutations(lists,n))
print(kindOfLine)
n = int(input())
ineq = list(input().split(" "))
number = [0,1,2,3,4,5,6,7,8,9]
from itertools import permutations
can = list(permutations(number,len(ineq)))    
tt= []
for i in range(len(ineq)):
    if ineq[i] == '<':
        tt.append("a")
    else:
        tt.append("b")
last_can = []
for j in can:
    bb = []
    for i in range(len(j)-1):
        if j[i]<j[i+1]:
            bb.append("a")
        else:
             bb.append("b")
    if j[len(j)-1]>j[len(j)-2]:
        bb.append("a")
    else:
        bb.append("b")
    if bb == tt:
        last_can.append(j)

l = len(last_can)
for i in range(len(ineq)):
    print(last_can[l-1][i],end="")
print()
for i in range(len(ineq)):
    print(last_can[0][i],end="")
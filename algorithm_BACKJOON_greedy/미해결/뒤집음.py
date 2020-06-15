n = int(input())
p = 1
while True:
    q=""    
    q_list = list(str(p))
    q_list.reverse()
    for i in q_list:
        q+=i
    if (p - (int(q))) == n:
        print(p)
        break
    else:
        p+=1

'''
조건1) n = 9의배수
조건2) 
'''
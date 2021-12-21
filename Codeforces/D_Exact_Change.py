from sys import maxsize
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ok1,ok2,ok3,ok4,ok5 = 0,0,0,0,0
    v = maxsize
    for i in range(n):
        if (l[i] % 3 != 0):
            ok1 = v
            break 
        ok1 = max(ok1, l[i]//3)
    for i in range(n):
        if l[i] % 3 == 2 :
            ok2 = v
            break
        ok2 = max(ok2, l[i] // 3)
    for i in range(n):
        if l[i] % 3 == 1 :
            ok3 = v
            break
        ok3 = max(ok3, l[i] // 3)
    for i in range(n):
        if l[i] % 3 == 0:
            ok4 = max(ok4, l[i] // 3 - 1);
        else:
            ok4 = max(ok4, l[i] // 3)
    for i in range(n):
        if l[i] == 1:
            ok5 = v
            break
        if l[i] % 3 == 1:
            ok5 = max(ok5, (l[i] -4) // 3);
        else:
            ok5 = max(ok5, l[i] // 3)
    ok2+=1
    ok3+=1
    ok5+=2
    ok4+=2
    print(min(ok1,ok2,ok3,ok4,ok5))
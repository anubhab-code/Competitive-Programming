for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    check,p,temp = 1,0,0
    for i in a:
        if temp:
            if i!=0:
                check = 0
                continue
        p += i
        if p==0:
            temp = 1
        elif p<0:
            check = 0
    if check and not p:
        print("Yes")
    else:
        print("No")
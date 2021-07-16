for _ in range(int(input())):
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    flag=2
    if len(set(l)) == 1 and l[0] == x:
        flag=0
    elif x in l or sum([i-x for i in l])==0:
        flag=1
    if flag==0:
        print(0)
    elif flag==1:
        print(1)
    else:
        print(2)

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    check=0
    for j in range(n):
        if l[j]!=j+1:
            check=1
    if check==0:
        print(0)
    elif l[0]== n and l[-1]==1:
        print(3)
    elif l[0]==1 or l[-1]==n:
        print(1)
    else:
        print(2)
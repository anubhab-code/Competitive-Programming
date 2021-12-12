for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    flag=1
    for i in range(n):
        if i:
            if a[i]-a[i-1]>=2:
                flag=0
    if flag:
        print("Yes")
    else:
        print("No")
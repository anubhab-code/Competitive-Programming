for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n%2==0:
        print("YES")
    else:
        flag=0
        for i in range(n-1):
            if l[i]>=l[i+1]:
                flag=1
                break
        if not flag:
            print("NO")
        else:
            print("YES")
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag = 0
    for i in range(n-2):
        if l[i]<l[i+1] and l[i+1]>l[i+2]:
            flag=1
            break
    if flag:
        print("YES")
        print(i+1,i+2,i+3)
    else:
        print("NO")
            
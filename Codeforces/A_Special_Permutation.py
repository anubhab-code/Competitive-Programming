for i in range(int(input())):
    n=int(input())
    l=[i  for i in range(n,0,-1)]
    if n%2!=0:
        l[-1]=l[n//2]
        l[n//2]=1
    print(*l)

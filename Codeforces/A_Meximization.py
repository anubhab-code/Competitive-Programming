for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    a1=[]
    for i in range(n-1):
        if l[i]==l[i+1]:
            a1.append(l[i])
    a2=set(l)
    a2=sorted(a2)
    print(*a2,*a1)
    
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    new=[]
    if n%2!=0:
        for i in range(n//2):
            new.append(a[i])
            new.append(a[n-i-1])
        new.append(a[n//2])
        
    else:
        for i in range(n//2):
            new.append(a[i])
            new.append(a[n-i-1])
    for i in range(n):
        print(new[i],end=' ')
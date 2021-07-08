for _ in range(int(input())):
    n,k=map(int,input().split())
    l = [0,1,3,1]+[0 for i in range(n)]
    a,b=2,3
    for i in range(n):
        if i<=3:
            print(l[i])
        else:
            j=i
            while j%2==0:
                j=j//2
            if j==1:
                a*=2
                b+=a 
                l[i]=b 
            else:
                l[i]=l[i-a]
            print(l[i])
        t=int(input())
        if t==1:
            break
        if t==-1:
            exit(0)
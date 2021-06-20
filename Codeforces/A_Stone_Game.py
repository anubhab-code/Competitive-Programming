for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=l.index(max(l))+1
    y=l.index(min(l))+1
    s1=max(x,y)
    s2=min(x+n-y+1,y+n-x+1)
    s3=max(n-x,n-y)+1
    print(min(s1,s2,s3))
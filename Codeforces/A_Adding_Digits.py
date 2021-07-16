a,b,n=map(int,input().split())
a=a*10
if a%b==0:
    print(str(a)+'0'*(n-1))
else:
    f=0
    for i in range(1,10):
        if (a+i)%b==0:
            a=a+i
            f=1
            break
    if f==1:
        a=str(a)+'0'*(n-1)
        print(a)
    else:
        print(-1)
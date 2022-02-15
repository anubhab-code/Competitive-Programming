n=int(input())
a=list(map(int,input().split()))
mn=min(a)
div=n//mn
if div==0:
    print(-1)
    exit()
 
 
for i in range(div):
    for j in range(8,-1,-1):
        if (div-i-1)*mn<=n-a[j]:
            print(j+1,end="")
            n-=a[j]
            break
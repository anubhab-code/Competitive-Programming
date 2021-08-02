from math import gcd

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=[abs(l[i]-l[i+1]) for i in range(n-1)]
    n-=1
    f=0
    new=[0]*(n+1)
    for i in range(2,n+1):
        new[i]=new[i>>1]+1
    temp=[]
    for i in range(20):
        temp.append([0]*(n+1))
        
    for i in range(new[n]+1):
        j=0
        keke=2**i
        while j+keke<=n:
            if keke==1:
                lmao=l[j]
                temp[i][j]=lmao
            else:
                hoho=j+(keke//2)
                lmao=gcd(temp[i-1][hoho],temp[i-1][j])
                temp[i][j]= lmao
            j+=1
    last,high,ans=1,n,0
    while last<=high:
        dekhle=0
        m=(last+high)//2
        for i in range(0,n-m+1):
            a=i
            b=i+m-1
            p=new[b-a+1]
            check=gcd(temp[p][b-(2**p)+1],temp[p][a])
            if check>1:
                dekhle=1
                break
        if dekhle:
            last=m+1
            ans=m+1
        else:
            high=m-1
            
    if ans<=1:
        print(1)
    else:
        print(ans)
def hehe(num,x,k):
    ans=0
    ans+=(min(num,k)*(min(num,k)+1))//2
    num-=min(num,k)
    a = k-1
    d = -1
    n = num
    temp = num*(2*a+(n-1)*d)
    temp//=2
    ans+=temp
    if(ans>=x):
        return False
    else:
        return True
    

for _ in range(int(input())):
    k,x=map(int,input().split())
    l,h=1,2*k-1
    while l<h:
        m=(l+h)//2
        if hehe(m,x,k):
            l=m+1
        else:
            h=m
    print(l)
    
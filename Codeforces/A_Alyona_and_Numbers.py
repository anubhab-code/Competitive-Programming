def fun(x,y):
    final=0
    for i in range(1,x+1):
        if i%5==y:
            final+=1
    return final

n,m=map(int,input().split())
ans=0
ans+=fun(n,0)*fun(m,0)
ans+=fun(n,1)*fun(m,4)
ans+=fun(n,2)*fun(m,3)
ans+=fun(n,3)*fun(m,2)
ans+=fun(n,4)*fun(m,1)
print(ans)
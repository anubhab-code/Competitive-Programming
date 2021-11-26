def hehe(n):
    final=n
    while n>0:
        final+=n%10
        n=n//10
    return final

n=int(input())
ans=[]
for i in range(n-81,n+1):
    if hehe(i)==n:
        ans.append(i)
print(len(ans))
print(*ans)
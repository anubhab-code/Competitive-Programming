n = int(input())
l = list(map(int,input().split()))
ans = sum(l)
x=[]
for i in range(3,n):
    if n%i==0:
        x.append(i)
for i in x:
    for j in range(n//i):
        ans = max(ans,sum(l[j::n//i]))
print(ans)
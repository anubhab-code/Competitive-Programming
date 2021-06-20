n = int(input())
p,p2 = 0,0
l = list(map(int,input().split()))
for i in range(n):
    if l[i]==1:
        p=i+1
    if l[i]==n:
        p2=i+1
print(max(p-1,p2-1,n-p,n-p2))
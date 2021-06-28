n = int(input())
l = list(map(int, input().split()))
ans = 0
c = 1
temp = l[0]
for i in range(1, n):
    if temp==l[i]:
        c+=1
    else:
        ans+=((c*(c+1))//2)
        c=1
        temp=l[i]
print(ans+(c*(c+1))//2)
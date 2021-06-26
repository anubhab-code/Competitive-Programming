n = int(input())
l = list(map(int,input().split()))
ans = 0
for i in range(n):
    c=i
    while c+1<n and l[c]<=l[c+1]: 
        c+=1
    while c+1<n and l[c]>=l[c+1]: 
        c+=1
    ans = max(c-i+1,ans)
print(ans)
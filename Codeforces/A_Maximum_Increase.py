n = int(input())
l = list(map(int,input().split()))
ans = 1
temp = 1
for i in range(n-1):  
    if l[i+1]>l[i]:
        temp+=1
    else:
        temp = 1
    ans = max(temp,ans)
print(ans)
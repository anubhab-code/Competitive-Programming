n = int(input())
l = list(map(int,input().split()))
temp = 0
ans = []
for i in l:
    ans.append(i+temp)
    if i>0:
        temp+=i
print(*ans)
n = int(input())
l = list(map(int,input().split()))
ans,curr = l[-1],l[-1]
temp = l[:-1][::-1]
for i in temp:
    curr = min(curr-1,i)
    if curr <= 0:
        break
    ans += curr
print(ans)
n = int(input())
l = list(map(int,input().split()))
t = sum(l)
temp = sorted(l)[-2::]
ans = []
for i,ele in enumerate(l):
    if ele!=temp[1]:
        if t-ele==2*temp[1]:
            ans.append(i+1)
    else:
        if t-ele==2*temp[0]:
            ans.append(i+1)
print(len(ans))
print(*ans)
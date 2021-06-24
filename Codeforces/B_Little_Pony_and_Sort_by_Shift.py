n = int(input())
l = list(map(int,input().split()))
ans = 0
flag = 0
for i in range(1, n):
    if l[i] < l[i-1]:
        ans = n-i
        flag += 1
if (flag == 1 and l[0] >= l[-1]) or flag == 0:
    print(ans)
else:
    print(-1)
n = int(input())
l = []
for i,j in enumerate(map(int,input().split())):
    l.append((j,i))
l=sorted(l)
mx = -1
ans = [0]*n
for val,i in l:
    mx = max(mx,i)
    ans[i] = mx-i-1
print(*ans)
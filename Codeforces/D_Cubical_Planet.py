l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
ans = 0
for i in range(3):
    ans+=abs(l1[i]-l2[i])
if ans==3:
    print("NO")
else:
    print("YES")
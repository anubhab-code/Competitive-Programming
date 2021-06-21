arr = []
for x in range(100):
    arr.append([])
    arr[x] = [0 for i in range(100)]
n = int(input())
ans=0
for x in range(n):
    a, b, c, d = map(int, input().split())
    ans=ans+(c-a+1)*(d-b+1)
print(ans)
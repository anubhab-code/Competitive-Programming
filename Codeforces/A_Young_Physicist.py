n = int(input())
arr = []
flag = 0
for _ in range(n):
    arr.append(list(map(int,input().split())))
for i in range(len(arr[0])):
    s = 0
    for j in range(n):
        s += arr[j][i]
    if s == 0:
        continue
    else:
        flag = 1
        break
if flag == 1:
    print("NO")
else:
    print("YES")
n = int(input())
data = list(map(int,input().split()))
hundred = data.count(100)
if len(data) == 1:
    print("NO")
elif hundred == 0 and len(data) % 2 == 1:
    print("NO")
elif hundred % 2 == 0:
    print("YES")
else:
    print("NO")
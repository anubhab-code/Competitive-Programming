n,t = map(int,input().split())
l = list(map(int,input().split()))
flag,i = 0,1
while i<=t:
    if i==t:
        flag = 1
        print("YES")
        break
    i += l[i-1]
if not flag:
    print("NO")
ans=[]
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = min(l)
    temp = l
    temp=sorted(temp)
    flag = 1
    for i in range(n):
        if l[i] % m != 0:
            if l[i] != temp[i]:
                flag = 0
                break
    if flag==1:
        ans.append("YES")
    else:
        ans.append("NO")
print('\n'.join(ans))
n = int(input())
l = list(map(int,input().split()))
z = l.count(0)
o = l.count(1)
if z>=o:
    ans = []
    temp = 0
    l=l[::-1]
    for i in range(n):
        if l[i]==0:
            temp+=1
        else:
            ans.append(temp)
    # print(ans)
else:
    ans = []
    temp = 0
    for i in range(n):
        if l[i]==1:
            temp+=1
        else:
            ans.append(temp)
    # print(ans)
print(sum(ans))
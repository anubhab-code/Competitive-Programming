n = int(input())
p = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
temp = []
for i in range(len(p)):
    temp.append([p[i],a[i],b[i]])
temp=sorted(temp,key=lambda x:x[0])
check=[0]*4
ans=[]
for i in range(len(c)):
    curr=c[i]
    while check[curr]<len(p):
        if temp[check[curr]][1] == curr or temp[check[curr]][2] == curr:
            ans.append(temp[check[curr]][0])
            temp[check[curr]][1] = 0
            temp[check[curr]][2] = 0
            break
        # break
        check[curr] += 1
        # break
    if check[curr] == len(p):
        ans.append(-1)
print(*ans)
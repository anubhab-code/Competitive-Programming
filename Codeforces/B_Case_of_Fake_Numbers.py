n = int(input())
l = list(map(int,input().split()))
while l[0]!=0:
    for i in range(n):
        if i%2==0:
            if l[i]!=n-1:
                l[i]+=1
            else:
                l[i]=0
        else:
            if l[i]!=0:
                l[i]-=1
            else:
                l[i]=n-1
check = 0
for j in range(1,n):
    if l[j]-l[j-1] != 1:
        check = 1
        break
if check==0:
    print('Yes')
else:
    print('No')
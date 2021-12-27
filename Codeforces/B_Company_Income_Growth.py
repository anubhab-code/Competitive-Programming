n=int(input())
p=2000
a=list(map(int,input().split()))
ans=[]
income=0
for i in range(len(a)):
    if a[i]>0 and a[i]-income==1:
        ans.append(p+(i+1))
        income=a[i]
print(len(ans))
if len(ans)==0:
    exit()
print(*ans)
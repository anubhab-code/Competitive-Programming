n=int(input())
arr=[]
l=[]
for _ in range(n):
    s,r,h,c=map(int,input().split())
    arr.append([s,r,h,c])
for i in range(n):
    for j in range(n):
        if i!=j and arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1] and arr[i][2]<arr[j][2]:
            arr[i][3]=1001
for i in arr:
    l.append(i[3])
print(l.index(min(l))+1)
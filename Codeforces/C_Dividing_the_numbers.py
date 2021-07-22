n=int(input())
arr=[]
if n%4==0:
    ans=0
    for x in range(1,n+1):
        if x%4==1 or x%4==0:
            arr.append(x)
if n%4==1:
    ans=1
    for x in range(1,n+1):
        if x%4==2 or x%4==1:
            arr.append(x)
if n%4==2:
    ans=1
    for x in range(1,n+1):
        if x%4==3 or x%4==2:
            arr.append(x)
if n%4==3:
    ans=0
    for x in range(1,n+1):
        if x%4==0 or x%4==3:
            arr.append(x)
print(ans)
print(len(arr),end=" ")
print(*arr)
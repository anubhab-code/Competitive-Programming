n,k=map(int,input().split())
arr=list(map(int,input().split()))
brr=[int(i) for i in arr]
brr.sort()
if brr[-1]-brr[0]>k:
    print("NO")
    exit()
print("YES")
for i in arr:
    for j in range(1,i+1):
        x=j%k if j%k!=0 else k
        print(x,end=" ")
    print()
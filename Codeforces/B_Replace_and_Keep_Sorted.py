n,q,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(q):
    l,r=map(int,input().split())
    # print(a[l-1])
    # print(a[r-1])
    print((a[l-1]-1)+(((a[r-1]-a[l-1]+1)-(r-l)-1)*2)+(k-a[r-1]))
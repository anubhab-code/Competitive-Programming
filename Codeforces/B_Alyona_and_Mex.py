n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
mex=1
for i in l:
    if i>=mex:
        mex+=1
print(mex)
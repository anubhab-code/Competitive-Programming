n=int(input())
a=list(map(int,input().split()))
maxdiff=max(a)-min(a)
if maxdiff==0:
    print(maxdiff,(n*(n-1))//2)
else:
    print(maxdiff,a.count(min(a))*a.count(max(a)))
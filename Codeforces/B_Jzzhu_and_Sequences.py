f1,f2=map(int,input().split())
n=int(input())
n%=6
l=[f1,f2,f2-f1,-f1,-f2,-f2+f1]
print(l[n-1]%1000000007)
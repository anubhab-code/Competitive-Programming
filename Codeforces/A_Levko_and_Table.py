n,m=map(int,input().split())
n-=1
for i in range(n+1):
    print('0 '*i+str(m)+' 0'*(n-i))
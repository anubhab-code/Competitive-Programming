n,k = list(map(int,input().split()))
end = (n+1)//2
if k > end:
    print(2*(k-end))
else:
    print(2*(k)-1)
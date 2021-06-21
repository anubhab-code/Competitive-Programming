n,d = list(map(int,input().split()))
song = list(map(int,input().split()))
if sum(song)+(n-1)*10 > d:
    print(-1)
elif sum(song)+(n-1)*10 == d:
    print((n-1)*2)
else:
    print((n-1)*2+((d-sum(song)-(n-1)*10)//5))
n,m=map(int,input().split())
ac=list(map(int,input().split()))
wa=list(map(int,input().split()))
ac=sorted(ac)
wa=sorted(wa)
if ac[0]*2>=wa[0] or ac[-1]>=wa[0]:
    print(-1)
else:
    print(max(ac[0]*2,ac[-1]))
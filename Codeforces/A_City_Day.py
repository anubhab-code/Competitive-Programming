n,x,y = map(int,input().split())
l = list(map(int,input().split()))
i = 0
while l[i]>min(l[max(0,i-x):i+y+1]):
    i+=1
ans = i+1
print(ans)
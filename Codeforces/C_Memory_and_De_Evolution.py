x,y = map(int,input().split())
ans = 0
a=b=c=y
while not (a>=x and b>=x and c>=x):
    if ans%3==0:
        a = b+c-1
    elif ans%3==1:
        b = a+c-1
    else:
        c = a+b-1
    ans += 1
print(ans)
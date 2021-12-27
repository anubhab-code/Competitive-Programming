for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    x,x1,y,y1 = 0,0,0,0
    for i in range(n):
        if a[i]==b[i]:
            x+=1
            if a[i]=='1':
                x1+=1
        else:
            y+=1
            if a[i]=='1':
                y1+=1
    flag = 1
    ans = 10**9
    if x%2!=0 and (x+1)//2==x1:
        ans = x
        flag = 0
    if y%2==0 and y//2==y1:
        ans = min(ans,y)
        flag = 0
    if flag:
        print(-1)
    else:
        print(ans)
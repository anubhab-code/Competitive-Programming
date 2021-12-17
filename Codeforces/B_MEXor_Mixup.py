def solve(n):
    a=n
    if a % 4 == 0 :
        return a
    if a % 4 == 1 :
        return 1
    if a % 4 == 2 :
        return a + 1
    return 0

for _ in range(int(input())):
    x,y=map(int,input().split())
    ans=solve(x-1)
    ans=ans^y
    if ans!=0:
        if ans!=x:
            x+=1
        else:
            x+=2
    print(x)
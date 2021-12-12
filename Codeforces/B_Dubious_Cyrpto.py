for _ in range(int(input())):
    l,r,m=map(int,input().split())
    ma=r-l
    for i in range(l,r+1):
        temp=m%i
        if temp<=ma and i<=m:
            print(i,l+temp,l)
            break
        elif i-temp<=ma:
            print(i,l,l+i-temp)
            break
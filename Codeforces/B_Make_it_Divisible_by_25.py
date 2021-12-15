for _ in range(int(input())):
    n=int(input())
    m=n
    k1=0
    while m!=0:
        if m%10==5:
            break
        m=m//10
        k1+=1
    if m%10==5:
        m=m//10
    flag=0
    while(m!=0):
        if m%10==2 or m%10==7:
            flag=1
            break
        k1+=1
        m=m//10
    if flag==0:
        k1=float('INF')
    k2=0
    m=n
    while(m!=0):
        if m%10==0:
            break
        m=m//10
        k2+=1
    if m%10==0:
        m=m//10
    flag=0
    while(m!=0):
        if m%10==5 or m%10==0:
            flag=1
            break
        k2+=1
        m=m//10
    if flag==0:
        k2=float('INF')
    ans=min(k1,k2)
    print(ans)
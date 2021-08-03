for _ in range(int(input())):
    n=int(input())
    s=[]
    tr,td,bu,bl=0,0,0,0
    for i in range(n):
        s.append(input())
        if i==0:
            tr=s[i][1]
        if i==1:
            td=s[i][0]
        if i==n-2:
            bu=s[i][n-1]
        if i==n-1:
            bl=s[i][n-2]
    ans=[]
    if tr==td:
        if bu==tr:
            ans.append((n-1,n))
        if bl==tr:
            ans.append((n,n-1))
    elif bu==bl:
        if tr==bu:
            ans.append((1,2))
        if td==bu:
            ans.append((2,1))
    else:
        if bu!=tr:
            ans.append((n-1,n))
            ans.append((1,2))
        elif bl!=tr:
            ans.append((n,n-1))
            ans.append((1,2))
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])
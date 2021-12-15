for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l2=l.copy()
    l2=sorted(l2)[::-1]
    final = []
    ans = 0
    for i in range(n):
        temp = l.index(l2[i])
        for j in range(temp+1,n-i):
            l[j-1]= l[j]
        l[n-i-1] = l2[i]
        if n-i-1==temp:
            continue
        else:
            ans += 1
            final.append([min(n-i,temp+1),max(n-i,temp+1),1])
    print(ans)
    for k in final:
        print(k[0],k[1],k[2])

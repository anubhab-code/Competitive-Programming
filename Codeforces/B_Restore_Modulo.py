for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    if len(set(l))==1 or n<=2:
        print(0)
    else:
        dif = []
        flag = True
        for i in range(n-1):
            if l[i+1]-l[i]!=0: 
                dif.append(l[i+1]-l[i])
            else: 
                flag = False
        i = len(set(dif))
        if not flag or i>2: 
            print(-1)
        elif i<=1:
            print(0)
        else:
            c = max(dif)
            m = c - min(dif)
            ans = [l[0] for j in range(n)]
            for i in range(1,n):
                ans[i] = (ans[i-1]+c)%m
            if ans==l and ans[0]<m and m>0 and c>0: 
                print(m,c)
            else: 
                print(-1)
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = 10**9+7
    d = {}
    for i in l:
        if i not in d:
            d[i]=0
        d[i]+=1
    temp,s = [],0
    for i in d.values():
        temp.append(i)
        s+=i
    lt = len(temp)
    temp = sorted(temp)
    for i in range(lt):
        t1 = s-(lt-i)*temp[i]
        ans = min(t1,ans)
    print(ans)
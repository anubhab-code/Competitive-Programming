for _ in range(int(input())) :
    n = int(input())
    l = list(map(int,input().split()))
    ans,temp,t1 = 0,[],0
    for i in l:
        x = i
        t = 0
        if i%2==1:
            t1 = 1
        while x%2==0:
            t += 1
            x//=2
        temp.append(t)
        ans += t
    temp=sorted(temp)[::-1]
    if t1 == 0:
        t1 = 1
        temp.pop()
    if t1:
        for i in range(len(temp)) :
            if temp[i] > 1:
                ans -= temp[i]
                ans += 1
            else :
                break
    print(ans)
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = [0,0,0]
    for i in l:
        c[i%3]+=1
    ans,avg = 0,n//3
    if c[0] < avg:
        ans += avg-c[0]
        c[2] -= avg-c[0]
    else:
        ans += c[0]-avg
        c[1] += c[0]-avg
    if c[1] < avg:
        ans += 2*(avg-c[1])
        c[2] -= avg-c[1]
    else:
        ans += c[1]-avg
        c[2] += c[1]-avg
    print(ans)
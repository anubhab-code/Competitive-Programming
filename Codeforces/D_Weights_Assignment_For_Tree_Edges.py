for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l1 = list(map(int,input().split()))
    l2 = [-1]*n
    l3 = [0]*n
    ans = 0
    flag = 1
    for i in range(n):
        temp = l1[i]-1
        if i==0:
            if l[temp]!=l1[i]:
                flag = 0
                break
            else:
                l2[temp] = 0
                
        else:
            if l2[l[temp]-1]==-1:
                flag = 0
                break
            else:
                check=l2[l[temp]-1]
                l2[temp] = max(check + 1,ans+1)
                ans = l2[temp]
                l3[temp] = l2[temp] - l2[l[temp]-1]
    if flag:
        print(*l3)
    else:
        print(-1)
t=int(input())
for _ in range(t):
    n,x = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    if _ < t-1:
        s = input()
    l1.sort()
    l2.sort(reverse = True)
    flag = 1
    for i in range(n):
        if l1[i] + l2[i] > x:
            flag = 0
            break
    if flag:
        print('Yes')
    else:
        print('No')
for _ in range(int(input())) :
    n = int(input())
    ans = [[0 for i in range(n)] for j in range(n)]
    for i in range(n-1) :
        ans[i][n-i-1] = 1
        ans[i][n-i-2] = 1
    ans[n-1][0] = 1
    ans[n-1][n-1] = 1
    for i in ans:
        print(*i)
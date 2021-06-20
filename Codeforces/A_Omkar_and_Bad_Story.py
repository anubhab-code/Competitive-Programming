for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    flag = 0
    for i in arr:
        if i < 0:
            flag = 1
            break
    if flag:
        print('NO')
        continue
    for i in range(max(arr)):
        if i not in arr:
            arr.append(i)
    print('YES')
    print(len(arr))
    print(*arr)
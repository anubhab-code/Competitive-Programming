for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [0] + arr
    found = [0]*(n + 1)
    for i in range(1, n + 1):
        if found[arr[i]] == 0:
            parent = arr[i]
            cycle = [parent]
            if arr[i] == i:
                found[arr[i]] = 1
                continue
            j = arr[arr[i]]
            while j != parent:
                cycle.append(j)
                j = arr[j]
            for i in cycle:
                found[i] = len(cycle)
    found.pop(0)
    print(*found)
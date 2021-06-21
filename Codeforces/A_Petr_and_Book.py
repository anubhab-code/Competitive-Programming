n = int(input())
d = list(map(int, input().split()))

while n > 0:
    for i in range(0,7):
        n -= d[i]
        if n <= 0:
            print(i+1)
            break
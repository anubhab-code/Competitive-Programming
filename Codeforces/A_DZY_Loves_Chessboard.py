n, m = list(map(int, input().split()))
for i in range(n):
    data = input()
    for j in range(len(data)):
        if data[j] == '.' and (j+i) % 2 == 0:
            print("B", end='')
        elif data[j] == '.':
            print("W", end='')
        else:
            print(data[j], end='')
    print("")
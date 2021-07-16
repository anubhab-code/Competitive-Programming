h,w = map(int,input().split())
r = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 1
mat = []
for i in range(h+1):
    o = [0]*(w+1)
    mat.append(o)
for row in range(h):
    col = r[row]
    for x in range(col):
        if mat[row][x] == 0:
            mat[row][x] = 1

    mat[row][col] = 2
for col in range(w):
    row = c[col]
    for x in range(row):
        if mat[x][col] == 2:
            print(0)
            exit()
        else:
            mat[x][col] = 1
    if mat[row][col] == 1:
        print(0)
        exit()
    else:
        mat[row][col] = 2
for row in range(h):
    for col in range(w):
        if mat[row][col] == 0:
            ans = (ans*2)%((10**9)+7)
print(ans)
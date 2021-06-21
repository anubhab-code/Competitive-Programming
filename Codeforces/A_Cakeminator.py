r,c = list(map(int,input().split()))
matrix = []
cakes = 0
for i in range(r):
    dat = input()
    if dat.count('S') != 0:
        matrix.append(dat)
    else:
        cakes += c
for i in range(c):
    flag = 0
    for j in range(len(matrix)):
        if matrix[j][i] == 'S':
            flag = 1
            break     
    if flag == 0:
        cakes += len(matrix)
print(cakes)
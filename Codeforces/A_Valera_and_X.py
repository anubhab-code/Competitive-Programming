n = int(input())
matrix = []
diagf = 0
elemf = 0
for _ in range(n):
    matrix.append(input())
diag = matrix[0][0]
elem = matrix[0][1]
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            if matrix[i][j] != diag:
                diagf = 1
                break
        else:
            if matrix[i][j] != elem:
                elemf = 1
                break
    if diagf == 1 or elemf == 1:
        break
if diagf == 1 or elemf == 1 or diag == elem:
    print("NO")
else:
    print("YES")
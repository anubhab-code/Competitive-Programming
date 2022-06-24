for _ in range(int(input())):
    mat = [None for i in range(8)]
    input()
    for i in range(len(mat)):
        mat[i] = input()
    x,y = None,None
    for i in range(1,7):
        for j in range(1,7):
            if mat[i][j] != '#':
                continue
            if ((mat[i-1][j-1] == '#' and mat[i-1][j+1] == '#') and (mat[i+1][j-1] == '#' and mat [i+1][j+1] == '#')):
                x,y = i,j
                break
    print(x+1,y+1)
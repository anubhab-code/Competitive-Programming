def cartesian_neighbor(x,y):
    arr = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i,j) != (x,y):
                arr.append((i,j))
    return(arr)
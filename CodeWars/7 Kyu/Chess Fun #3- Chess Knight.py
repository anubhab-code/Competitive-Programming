def chess_knight(cell):
    x = '0abcdefgh'.index(cell[0])
    y = int(cell[1]) 
    jumps = [-2, -1, 1, 2,]
    counter = 0
    for i in jumps:
        for j in jumps:
            if abs(i) != abs(j) and x + i >= 1 and x + i <= 8 and y + j >= 1 and y + j <= 8:
                counter += 1    
    return counter
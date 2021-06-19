def make_2d_list(head,row,col):
    if col == 0:
        return [[]]
    out = []
    for i in range(0,row*col, col):
        x = []
        for j in range(i+head ,i+head+col):
            x.append(j)
        out.append(x)
    return out
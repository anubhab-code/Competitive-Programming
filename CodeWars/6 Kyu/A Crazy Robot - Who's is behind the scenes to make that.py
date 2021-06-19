def finaldist_crazyrobot(moves, init_pos):
    x,y = init_pos[0],init_pos[1]
    for m in moves: 
        if m[0] == 'R': x += m[1]
        if m[0] == 'L': x -= m[1]
        if m[0] == 'U': y += m[1]
        if m[0] == 'D': y -= m[1]
    return ((x-init_pos[0])**2+(y-init_pos[1])**2)**0.5
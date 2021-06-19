def cat_mouse(map_, moves):
    lines = map_.split('\n')
    cat = None
    mouse = None
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'C':
                cat = (i,j)
            elif lines[i][j] == 'm':
                mouse = (i,j)
    if cat and mouse:
        result = abs(cat[0] - mouse[0]) + abs(cat[1] - mouse[1])
        return "Caught!" if result <= moves else "Escaped!"
    else:
        return "boring without two animals"
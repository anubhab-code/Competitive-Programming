def get_neighbourhood(n_type, mat, coordinates):
    x, y = coordinates
    n_list = []
    
    try:
        a=mat[x][y]
        
        if n_type == 'moore':
            for dx in range(-1,2): 
                for dy in range(-1,2):
                    if (dx!=0 or dy!=0) and ( (x+dx)>=0 and (y+dy)>=0 ):
                        try:
                            n_list.append(mat[x+dx][y+dy])
                        except: pass
                            
        else:
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if (abs(dx)!=abs(dy)) and ( (x+dx)>=0 and (y+dy)>=0 ):
                        try:
                            n_list.append(mat[x+dx][y+dy])
                        except: pass
    except: pass                    
    return n_list
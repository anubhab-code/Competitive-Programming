def get_neighbourhood(t, a, c, d=1):
    r, t = [], t == "von_neumann"
    x, y = c
    if x < len(a) and y < len(a[0]):
        for i in range(-d, d+1):
            for j in range(-d+abs(i)*t, d-abs(i)*t+1):
                try:
                    if x+i >= 0 and y+j >= 0 and (i or j): r.append(a[x+i][y+j])
                except: pass
    return r
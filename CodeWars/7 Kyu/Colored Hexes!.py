def hex_color(codes):
    if not codes: return 'black'
    r,g,b=map(int,codes.split(' '))
    max_v=max(r,g,b)
    if max_v==0:
        return 'black'
    elif r==g==b:
        return 'white'
    elif r==b==max_v:
        return 'magenta'
    elif g==r==max_v:
        return 'yellow'
    elif b==g==max_v:
        return 'cyan'
    elif r==max_v:
        return 'red'
    elif g==max_v:
        return 'green'
    else:
        return 'blue'
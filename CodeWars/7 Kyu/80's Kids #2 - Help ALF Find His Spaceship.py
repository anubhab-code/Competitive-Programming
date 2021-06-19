def find_spaceship(amap):
    ab=amap.split('\n')[::-1]
    for i in ab:
        if 'X' in i:
            return[ i.index('X') , ab.index(i) ]
    return "Spaceship lost forever."
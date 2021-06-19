def array_madness(a,b):
    square=[]
    cube=[]
    for ele in a:
        square.append(ele**2)
    for e in b:
        cube.append(e**3)
    if sum(square)>sum(cube):
        return True
    else:
        return False
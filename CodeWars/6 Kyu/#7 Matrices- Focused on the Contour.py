def countour_mode(matrix, a, b):
    d={}
    for x in matrix[0]+matrix[-1]:
        if a<=x<=b:
            d[x]=d.get(x,0)+1
    for row in matrix[1:-1]:
        for i in [0,-1]:
            if a<=row[i]<=b:
                d[row[i]]=d.get(row[i],0)+1
    max_v=max(d.values())
    if min(d.values())==max_v:
        return []
    return [max_v,sorted([k for k,v in d.items() if v==max_v])]
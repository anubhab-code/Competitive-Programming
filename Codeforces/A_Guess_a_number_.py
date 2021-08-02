n = int(input())
maxr = 2 * 1000 * 1000 * 1000
minr = -maxr
for i in range(n):
    con, x, ans =  input().split()
    x = int(x)
    if(ans=='N'):
        if(con=='>='):
            con  = '<'
        elif(con=='<='):
            con = '>'
        elif(con == '<'):
            con = '>='
        else:
            con = '<='
    
    if(con == '>'):
        minr = max(minr, x+1)
    elif(con == '>='):
        minr = max(minr, x)
    elif(con == '<='):
        maxr = min(maxr, x)
    else:
        maxr = min(maxr, x-1)
        
if(minr<=maxr):
    print(minr)
else:
    print('Impossible')
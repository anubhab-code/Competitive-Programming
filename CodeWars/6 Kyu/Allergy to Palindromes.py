def count_pal(n):  
    d, total = 0, 0
    for i in range(0,n):
        d = 9 * 10**(i//2)
        total += d
        
    return [d, total]
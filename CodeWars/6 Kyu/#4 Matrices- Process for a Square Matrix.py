def avg_diags(m):
    a = []
    b = []
    for i in range(len(m)):
        if i % 2 == 1 and m[i][i] >= 0:
            a.append(m[i][i])
        
        if i % 2 == 0 and m[-i-1][i] < 0:
            b.append(m[-i-1][i])
                        
    a = round(sum(a) / len(a)) if len(a) else -1
    b = round(abs(sum(b) / len(b))) if len(b) else -1
    return [a, b]
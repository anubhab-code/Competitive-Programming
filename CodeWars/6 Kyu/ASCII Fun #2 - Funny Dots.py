def dot(n,m):
    r=['+'+'---+'*n]
    for _ in range(m):
        r.append('|'+' o |'*n)
        r.append('+'+'---+'*n)
    return '\n'.join(r)
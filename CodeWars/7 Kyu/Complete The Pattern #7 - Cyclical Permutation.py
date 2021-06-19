def pattern(n):
    t,f,end = '','',''
    for i in range(n):
        if i>=1:end += str(i)
        for j in range(i+1,n+1):
            t += str(j)
        f += t+end+'\n'
        t = ''
    return f[0:-1]
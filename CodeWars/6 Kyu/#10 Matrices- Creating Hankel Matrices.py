s=[]
n=1
for i in range(200): 
    s.append(n)
    n=2*n*(2*i+1)//(i+2)

def hankel_matrix_maker(n): 
    return [s[i:i+n] for i in range(n)]
def chessboard(s):
    s=s.split()
    a=int(s[0])
    b=int(s[1])
    A1=[]
    A2=[]
    for i in range(b):
        if i%2==0:
            A1.append("*")
            A2.append(".")
            
        else:
            A1.append(".")
            A2.append("*")
    A1="".join(A1)
    A2="".join(A2)
    B=[]
    for i in range(a):
        if i%2==0:
            B.append(A1)
        else:
            B.append(A2)
    return("\n".join(B))
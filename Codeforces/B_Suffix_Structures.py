def fun(s,t):
    c=0
    a=len(s)
    b=len(t)
    for i in range(a):
        if c<b and s[i]==t[c]:
            c+=1
    return c==b
    
s=input()
t=input()
ss=sorted(s)
st=sorted(t)
ss="".join(ss)
st="".join(st)
if fun(s,t):
    print("automaton")
elif ss==st:
    print("array")
elif fun(ss,st):
    print("both")
else:
    print("need tree")
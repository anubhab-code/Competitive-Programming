def alphabet_war(reinforces, airstrikes):
    n=len(reinforces[0])
    r=[]
    for _ in range(n):
        r.append([])
    for reinforce in reinforces:
        for i in range(n):
            r[i].append(reinforce[i])
    a=[]
    for i in range(n):
        a.append(r[i].pop(0))
    for airstrike in airstrikes:
        st=set()
        for i in range(len(airstrike)):
            if airstrike[i]=='*':
                st.add(i)
                if i>0: st.add(i-1)
                if i<n-1: st.add(i+1)
        for i in st:
            if r[i]:
                a[i]=r[i].pop(0)
            else:
                a[i]='_'
    return ''.join(a)
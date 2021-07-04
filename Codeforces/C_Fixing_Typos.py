s=input()
l=[]
n=len(s)
i=0
while i<n:
    if len(l)<2:
        l.append(s[i])
        i+=1
    else:
        if s[i]==l[-1]==l[-2]:
            i+=1
        elif len(l)>=3 and s[i]==l[-1] and l[-2]==l[-3]:
            i+=1
        else:
            l.append(s[i])
            i+=1
print("".join(l))
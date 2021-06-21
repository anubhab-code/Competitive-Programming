s1=input()
s2=""
i=0
while i<len(s1):
    if s1[i]=="-" and s1[i+1]=="-":
        s2=s2+"2"
        i=i+2
    elif s1[i]=="-" and s1[i+1]==".":
        s2=s2+"1"
        i=i+2
    else:
        s2=s2+"0"
        i=i+1
print(s2)
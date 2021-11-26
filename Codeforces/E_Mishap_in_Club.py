s=input()
ma,mi,p=0,0,0
for i in s:
    if i=="+":
        p+=1
        ma=max(p,ma)
    else:
        p-=1
        mi=min(p,mi)
print(ma-mi)
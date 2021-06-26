d1={}
d2={}
d3={}
for _ in range(int(input())):
    a,b=input().split()
    a=int(a)
    d1[b]=0
    d2[b]=0
    d3[b]=0
    for k in range(a):
        s=input()
        s=s.replace("-","")
        if len(set(s))==1:
            d1[b]+=1
        elif all(i>j for (i,j) in zip(s,s[1:])):
            d2[b]+=1
        else:
            d3[b]+=1
print('If you want to call a taxi, you should call: {}.'.format(', '.join(p for p,count in d1.items() if count == max(d1.values()))))
print('If you want to order a pizza, you should call: {}.'.format(', '.join(p for p,count in d2.items() if count == max(d2.values()))))
print('If you want to go to a cafe with a wonderful girl, you should call: {}.'.format(', '.join(p for p,count in d3.items() if count == max(d3.values()))))
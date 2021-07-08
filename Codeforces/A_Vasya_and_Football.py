from collections import *
s1=input()
s2=input()
n=int(input())
d=defaultdict(int)
for i in range(n):
    time,ty,num,col=map(str,input().split())
    d[ty+num+col]+=1
    if col=='y' and d[ty+num+col]==2 and d[ty+num+'r']==0:
        if ty=='a':
            print(s2,num,time)
        else:
            print(s1,num,time)
    elif col=='r' and d[ty+num+col]==1 and (d[ty+num+'y']==0 or d[ty+num+'y']==1):
        if(ty=='a'):
            print(s2,num,time)
        else:
            print(s1,num,time)
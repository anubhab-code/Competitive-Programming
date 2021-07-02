import math
a=int(input())
flag=0
for i in range(1,int(math.sqrt(a))+1):
    if(a%i==0):
        if(a/i==i):
            p=str(int(i))
            for j in range(0,len(p)):
                if(p[j] in str(a)):
                    flag=flag+1
                    break
        else:
            p=str(int(i))
            for j in range(len(p)):
                if(p[j] in str(a)):
                    flag=flag+1
                    break
            b=str(int(a/i))
            for j in range(len(b)):
                if b[j] in str(a):
                    flag=flag+1
                    break
print(flag)
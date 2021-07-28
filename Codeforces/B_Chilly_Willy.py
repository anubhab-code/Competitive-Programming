n=int(input())-1
if n>1:
    print(10**n+([1,1]+[110,50,80,170,20,200]*16667)[n])
else:
    print(-1)
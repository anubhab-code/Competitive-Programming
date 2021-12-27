def radix(x):
    k=[]
    while x:
        k.append(x%a)
        x//=a
    return ''.join(map(str,k))[::-1]
    
a=int(input())
for i in range(1,a):
    for j in range(1,a):
        print(radix(i*j),end=' ')
    print()
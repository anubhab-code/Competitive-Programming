n=int(input())
n=n+1
if len(set(str(n)))==4:
    print(int(n))
else:
    n=str(n)
    while len(set(n))!=4:
        n=int(n)
        n=n+1
        n=str(n)
    print(int(n))
def fun(a,n):
    if n==1:
        return a
    if int(min(str(a)))==0:
        return a
    return fun(a+int(max(str(a)))*int(min(str(a))), n-1)

for _ in range(int(input())):
    a,k = map(int,input().split())
    print(fun(a,k))
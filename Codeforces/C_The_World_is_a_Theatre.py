from math import factorial
def combo(n,k):
    num = factorial(n)
    den = factorial(n-k)
    num = num//den
    den = factorial(k)
    return num//den
n,m,t = map(int,input().split())
ans = 0
for i in range(4,n+1):
    men = i
    women = t-i
    if women>=1 and women<=m:
        men = combo(n,men)
        women = combo(m,women)
        ans+= men*women
print(ans)
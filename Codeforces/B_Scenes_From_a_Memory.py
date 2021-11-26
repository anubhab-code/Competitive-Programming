prime=[0]*100
for i in range(2,100):
    prime[i]=1
    j=2
    while j*j<=i:
        if i%j==0:
            prime[i]=0
        j+=1

def solve():
    n=int(input())
    s=input()
    for i in range(n):
        if int(s[i]) in [1,4,6,8,9]:
            print(1)
            print(s[i])
            return
    for i in range(n):
        for j in range(i+1,n):
            if not prime[int(s[i])*10+int(s[j])]:
                print(2)
                print(s[i]+s[j])
                return

for _ in range(int(input())):
    solve()
mod=10**9+7
n=int(input())
ans=6
ans=(ans*(pow(4,pow(2,n)-2,mod)))%mod
print(ans%mod)
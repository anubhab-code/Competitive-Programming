def pattern(n):
    ans=""
    i=1
    while i<=n:
        if len(ans)!=0:
            ans=ans+"\n"
        j=0
        while j<i:
            ans=ans+str(n-j)
            j=j+1
        i=i+1
    return ans
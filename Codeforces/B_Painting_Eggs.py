sa,sg=0,0
ans=''
for _ in range(int(input())):
    a,g=map(int,input().split())
    if sa-sg+a<=500:
        ans+='A'
        sa+=a
    else:
        ans+='G'
        sg+=g
print(ans)
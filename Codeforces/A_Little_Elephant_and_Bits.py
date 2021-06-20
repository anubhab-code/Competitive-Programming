n=input()
loc=n.find('0')
if loc==-1: 
    ans=n[1:]
else:
    ans=n[:loc]+n[loc+1:]
print(ans)
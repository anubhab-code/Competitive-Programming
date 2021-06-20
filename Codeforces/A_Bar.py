n=int(input())
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s="0123456789"
w={"ABSINTH","BEER", "BRANDY","CHAMPAGNE","GIN","RUM","SAKE","TEQUILA","VODKA","WHISKEY","WINE"}
ans=0
for i in range(n):
    i=input()
    if i[0] in s and int(i)<18:
        ans+=1
    elif i[0] in a and i in w:
        ans+=1
print(ans)
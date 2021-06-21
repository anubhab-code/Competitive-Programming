l=[]
for i in range(int(input())):
    l.append(input().split())
ans=[]
for i in l:
    if i[1]=='rat':
        ans.append(i[0])
for i in l:
    if i[1]=='woman' or i[1]=='child':
        ans.append(i[0])
for i in l:
    if i[1]=='man':
        ans.append(i[0])
for i in l:
    if i[1]=='captain':
        ans.append(i[0])
for i in ans:
    print(i)
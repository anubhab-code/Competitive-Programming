l1=[]
for i in range(0,3):
  l2=list(map(int,input().split()))
  l1.append(l2)
l3=[]
for i in range(0,3):
  l3.append(l1[i][0]+l1[i][1]+l1[i][2])
for i in range(0,3):
  l3.append(l1[0][i]+l1[1][i]+l1[2][i])
l3.append(l1[0][2]+l1[1][1]+l1[2][0])
 
c=max(l3)
j=1
while l1[0][2]+l1[1][1]+l1[2][0]!=l1[0][0]+l1[1][1]+l1[2][2]:
  l1[0][0]=c-l1[0][1]-l1[0][2]+j
  l1[1][1]=c-l1[1][0]-l1[1][2]+j
  l1[2][2]=c-l1[2][1]-l1[2][0]+j
  j=j+1
for x in l1:
  for y in x:
    print(y,end=" ")
  print()
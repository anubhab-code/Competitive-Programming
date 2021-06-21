n = int(input())
data = list(map(int,input().split()))
one , two , three = [] , [] , []
for i in range(len(data)):
    if data[i] == 1:
        one.append(i+1)
    elif data[i] == 2:
        two.append(i+1)
    else:
        three.append(i+1)
teams = min(len(one),len(two),len(three))
print(teams)
for i in range(teams):
    print(*[one[i],two[i],three[i]])
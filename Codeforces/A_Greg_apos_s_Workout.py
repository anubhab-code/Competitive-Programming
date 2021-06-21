n = int(input())
data = list(map(int,input().split()))
chest = sum(data[i] for i in range(0,len(data),3))
biceps = sum(data[i] for i in range(1,len(data),3))
back = sum(data[i] for i in range(2,len(data),3))
if max(chest,biceps,back)==chest:
    print("chest")
elif max(chest,biceps,back)==biceps:
    print("biceps")
else:
    print("back")
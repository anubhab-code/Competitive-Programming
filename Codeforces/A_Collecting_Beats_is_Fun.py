n=int(input())
arr=""
for i in range(4):
    arr=arr+input()
for i in range(1,10):
    if arr.count(str(i))>2*n:
        print("NO")
        exit()
print("YES")
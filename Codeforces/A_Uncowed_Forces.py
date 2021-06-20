marks=[500,1000,1500,2000,2500]
time=list(map(int,input().split()))
wrong=list(map(int,input().split()))
h,u=map(int,input().split())
ans=0
for i in range(5):
    ans=ans+max([0.3*marks[i],((1-time[i]/250)*marks[i])-(50*wrong[i])])
ans=ans+h*100-50*u
print(int(ans))
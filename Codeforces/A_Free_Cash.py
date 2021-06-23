n=int(input())
d={}
for i in range(n):
    s=input()
    try:
        d[s]=d[s]+1
    except:
        d[s]=1
print(max(d.values()))
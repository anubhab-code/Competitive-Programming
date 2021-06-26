n=int(input())
l=[]
c=ord("a")
for i in range(n):
    l.append(chr(c))
    c+=1
    if c==ord("e"):
        c=ord("a")
print("".join(l))

# n=int(input())
# print(("abcd"*(n//4))+"abcd"[:n%4])
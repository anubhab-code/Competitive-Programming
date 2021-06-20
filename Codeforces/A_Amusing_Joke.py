s1=input()
s2=input()
s3=input()

a = "".join(sorted(s1+s2))
b = "".join(sorted(s3))

if a==b:
    print("YES")
else:
    print("NO")
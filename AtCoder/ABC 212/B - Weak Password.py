def follow(a):
    if a == 9:
        return 0
    return a+1
string = input()
a,b,c,d = [int(x) for x in string]
if a == b and b == c and c == d :
    print("Weak")
elif follow(a) == b and follow(b) == c and follow(c) == d:
    print("Weak")
else:
    print("Strong")
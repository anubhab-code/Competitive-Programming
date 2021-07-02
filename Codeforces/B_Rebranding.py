n,m = map(int,input().split())
s = input()
l = [chr(ord('a')+i) for i in range(26)]
for i in range(m):
    a,b = input().split()
    for j in range(26):
        if l[j] == a:
            l[j] = b
        elif l[j] == b:
            l[j] = a
print(''.join([l[ord(k)-ord('a')] for k in s]))
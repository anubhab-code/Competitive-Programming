n = int(input())
l = [int(x) for x in input().split()]
st = set()
c = 0
for i in range(n):
    if l[i] != i:
        c += 1
        st.add((i, l[i]))
        st.add((l[i], i))
if c==0:
    print(n)
else:
    if c*2==len(st):
        print(len(l)+1-c)
    else:
        print(len(l)+2-c)
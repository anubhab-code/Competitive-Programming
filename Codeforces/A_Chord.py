a,b,c=map(str,input().split())
def pos(a,b):
    d={"C":1, "C#":2, "D":3, "D#":4, "E":5, "F":6, "F#":7, "G":8, "G#":9, "A":10, "B":11, "H":12}
    if d[a]<d[b]:
        return d[b]-d[a]
    else:
        return 12-d[a]+d[b]
l=[[a,b,c],[b,a,c],[a,c,b],[c,a,b],[b,c,a],[c,b,a]]
for i in l:
    if pos(i[0],i[1])==4 and pos(i[1],i[2])==3:
        print("major")
        exit()
    elif pos(i[0],i[1])==3 and pos(i[1],i[2])==4:
        print("minor")
        exit()
print("strange")
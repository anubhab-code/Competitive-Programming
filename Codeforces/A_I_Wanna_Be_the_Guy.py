l=set()
n=int(input())
p=list(map(int, input().split()))
q=list(map(int, input().split()))
l.update(p[1:])
l.update(q[1:])
if len(l)==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
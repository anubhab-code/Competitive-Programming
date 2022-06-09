#   _____  _____ _____     _____ _    _  _____ _    _          _   _ _______ 
#  |  __ \|_   _|  __ \   / ____| |  | |/ ____| |  | |   /\   | \ | |__   __|
#  | |__) | | | | |__) | | (___ | |  | | (___ | |__| |  /  \  |  \| |  | |   
#  |  _  /  | | |  ___/   \___ \| |  | |\___ \|  __  | / /\ \ | . ` |  | |   
#  | | \ \ _| |_| |       ____) | |__| |____) | |  | |/ ____ \| |\  |  | |   
#  |_|  \_\_____|_|      |_____/ \____/|_____/|_|  |_/_/    \_\_| \_|  |_|   
 
                                            
from collections import defaultdict, deque
 
n = int(input())
l = list(map(int, input().split()))
d,b,c = defaultdict(int),deque(),deque()
ans=[]
 
for i in range(n):
    d[l[i]] = i
 
for i in range(n+10):
    if i in d:
        b.append(i)
    else:
        c.append(i)
 
for i in range(n):
    t1 = c[0]
    t2 = b[0]
    if b and t1>t2 and i > d[t2]:
        t1 = b.popleft()
    else:
        t1 = c.popleft()
    ans.append(t1)
print(*ans)
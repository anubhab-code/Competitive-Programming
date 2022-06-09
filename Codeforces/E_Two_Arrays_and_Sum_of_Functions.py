#   _____  _____ _____     _____ _    _  _____ _    _          _   _ _______ 
#  |  __ \|_   _|  __ \   / ____| |  | |/ ____| |  | |   /\   | \ | |__   __|
#  | |__) | | | | |__) | | (___ | |  | | (___ | |__| |  /  \  |  \| |  | |   
#  |  _  /  | | |  ___/   \___ \| |  | |\___ \|  __  | / /\ \ | . ` |  | |   
#  | | \ \ _| |_| |       ____) | |__| |____) | |  | |/ ____ \| |\  |  | |   
#  |_|  \_\_____|_|      |_____/ \____/|_____/|_|  |_/_/    \_\_| \_|  |_|   
 
                                            
from collections import defaultdict, deque
 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    a[i] = a[i]*(i+1)*(n-i)
a=sorted(a)
b=sorted(b)[::-1]
for i in range(n):
    ans+=(a[i]*b[i])%998244353
print(ans%998244353)
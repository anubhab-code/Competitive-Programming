def is_lucky(n):
    digits = [int(x) for x in str(n)]
    for i in digits:
        if i not in [4,7]:
            return False
    else:
        return True
    
def almost_lucky(n):
    for i in range(4,n//2+1):
        if n % i == 0 and is_lucky(i):
            return True 
    return False

n = int(input())
if is_lucky(n) or almost_lucky(n):
    print("YES")
else:
    print("NO")
n = int(input())
ans = int(1.08 * n)
if ans > 206:
    print(":(")
elif ans == 206:
    print("so-so")
else:
    print("Yay!")
n = int(input())
a = input().rstrip()
s = list(map(int, [i for i in a]))
print("".join(map(str,min([(j+10-s[i])% 10 for j in (s[i:] + s[:i])] for i in range(n)))))
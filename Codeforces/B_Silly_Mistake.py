n = int(input())
a = list(map(int,input().split()))
ans = []
dic = set()
chk = set()
cnt,flag = 0,1
for i in a:
    cnt+=1
    if i in chk:
        flag = 0
        break
    if i>0:
        dic.add(i)
        chk.add(i)
    else:
        if abs(i) in dic:
            dic.remove(abs(i))
        else:
            flag = 0
            break
    if len(dic)==0:
        ans.append(cnt)
        cnt = 0
        chk = set()
if len(dic):
    flag = 0

if flag:
    print(len(ans))
    print(*ans)
else:
    print(-1)
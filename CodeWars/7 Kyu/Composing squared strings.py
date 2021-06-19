def compose(s1, s2):
    list1 = s1.split()
    list2 = s2.split()
    ans = []
    l = len(list1)
    for i in range(0,l):
        ans.append(list1[i][:(i+1)]+list2[l-1-i][:(l-i)])
    return "\n".join(ans)
def a1_thick_and_hearty(a1, a2):
    l = set(a1)&set(a2)
    l_sum = []
    for i in l:
      for ii in l:
        if i != ii:
            if i+ii == len(a1) or i+ii == len(a2):
                l_sum.append(ii)
                l_sum.append(i)
            if abs(i-ii) == len(a1) or abs(i-ii) == len(a2):
                l_sum.append(ii)
                l_sum.append(i)
    return set(l_sum)
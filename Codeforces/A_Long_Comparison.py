for _ in range(int(input())):
    x1,p1 = input().split()
    x2,p2 = input().split()
    n1 = len(x1) + int(p1)
    n2 = len(x2) + int(p2)
    if n1>n2:
        print(">")
    elif n1<n2:
        print("<")
    else:
        y1 = x1
        y2 = x2
        done = 0
        for i in range(n1):
            if i < min(len(x1),len(x2)):
                if y1[i]>y2[i]:
                    done = 1
                    print(">")
                    break
                elif y2[i]>y1[i]:
                    done = 1
                    print("<")
                    break
                else:
                    continue
            elif i >= len(x1) and i < len(x2):
                if y2[i]!='0':
                    #print(y2[i])
                    done = 1
                    print("<")
                    break
                else:
                    continue
            elif i >= len(x2) and i < len(x1):
                if y1[i] != '0':
                    done = 1
                    print(">")
                    break
                else:
                    continue
            else:
                break
        if done == 0:
            print("=")
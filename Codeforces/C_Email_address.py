m = input()
m = m.replace("at","@")
m = m.replace("dot",".")
if m[0] == ".":
    m = "dot" + m[1:]
if m[-1] == ".":
    m = m[:-1] + "dot"
if m[0] == "@":
    m = "at" + m[1:]
if m.count("@") > 1:
    n = m.find("@")
    m = m[:n+1] + m[n+1:].replace("@","at")
print(m)
s = "egg"
t = "add"
D = {}
for i in range(len(s)):
    if s[i] not in D:
        if t[i] in D.values():
            print(False)
        D[s[i]] = t[i]
    else:
        if D[s[i]] != t[i]:
            print(False)
print(True)
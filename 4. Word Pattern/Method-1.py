pattern = "abba"
s = "dog cat cat fish"
t = s.split()
D = {}
if len(pattern) != len(t):
    print(False)
if len(set(pattern)) != len(set(t)):
    print(False)
for i in range(len(t)):
    if t[i] not in D:
        D[t[i]] = pattern[i]
    else:
        if D[t[i]] != pattern[i]:
            print(False)
print(True)
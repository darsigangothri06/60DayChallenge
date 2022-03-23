n = 2
L = [1,2]
if n == 1:
    return 1
elif n == 2:
    return 2
else:
    for i in range(n-2):
        L.append(L[-1]+L[-2])
    return L[-1]
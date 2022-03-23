n = 4
L = [0,1,1]
if n == 0:
    return 0
elif n == 1:
    return 1
elif n == 2:
    return 1
else:
    for i in range(n-2):
        L.append(L[-1]+L[-2]+L[-3])
    return L[-1]
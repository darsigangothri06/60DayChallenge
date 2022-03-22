n = 3
k = 27
res, k, i = ['a'] * n, k - n, n - 1
while k:
    k += 1
    if k/26 >= 1:
        res[i], k, i = 'z', k - 26, i - 1
    else:
        res[i], k = chr(k + 96), 0

print(''.join(res))
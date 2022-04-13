D = {}
for i in arr:
    D[i] = D.get(i,0) + 1
    if D[i] / len(arr) > 0.25:
        return i
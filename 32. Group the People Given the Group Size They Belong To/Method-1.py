D = {}
op = []
for i in  range(len(groupSizes)):
    if groupSizes[i] not in D.keys():
        D[groupSizes[i]] = [i]
    else:
        if len(D[groupSizes[i]]) < groupSizes[i]:
            D[groupSizes[i]] += [i]
        else:
            op.append(D[groupSizes[i]])
            D[groupSizes[i]] = [i]                   
for i in D.values():
    op.append(i)
return op
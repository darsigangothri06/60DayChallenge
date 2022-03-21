intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
L = [intervals[0]]
for i in intervals[1:]:
    low = L[-1][0]
    high = L[-1][1]
    if i[0] <= high and i[1] > high:
        L[-1] = [low, i[1]]
    elif i[0] <= high and i[1] <= high:
        pass
    else:
        L.append(i)
print(L)
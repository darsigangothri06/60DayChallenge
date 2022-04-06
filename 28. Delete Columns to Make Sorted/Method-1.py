strs = ["rrjk","furt","guzm"]
sortedArray = []
for i in range(len(strs[0])):
    x = ''
    for j in range(len(strs)):
        x += strs[j][i]
    sortedArray.append(x)
print(sortedArray)
count = 0
for i in sortedArray:
    if i != ''.join(sorted(i)):
        count += 1
print(count)
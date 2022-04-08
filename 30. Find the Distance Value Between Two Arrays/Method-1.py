count = 0
for i in arr1:
    flag = True
    for j in arr2:
        if abs(i - j) <= d:
            flag = False
            break
    count += flag == True
return count
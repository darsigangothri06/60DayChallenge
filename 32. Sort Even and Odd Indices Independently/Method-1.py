even = sorted(nums[::2])
odd = sorted(nums[1::2], reverse = True)
x = []
i = 0
j = 0
while(i < len(even) and j < len(odd)):
    x.extend([even[i], odd[j]])
    i += 1
    j += 1
while(i < len(even)):
    x.append(even[i])
    i += 1
while(j < len(odd)):
    x.append(odd[j])
    j += 1
return x
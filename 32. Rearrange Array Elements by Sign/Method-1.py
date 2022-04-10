op = [None] * len(nums)
pos = 0
neg = 1
for i in nums:
    if i > 0:
        op[pos] = i
        pos += 2
    else:
        op[neg] = i
        neg += 2
return op
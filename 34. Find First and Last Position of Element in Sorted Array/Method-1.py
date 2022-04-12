if target not in nums:
    return [-1,-1]
if target in nums and nums.count(target) == 1:
    return [nums.index(target)] * 2
else:
    i = 0
    index = 0
    startIndex = 0
    flag = False
    while i < len(nums):
        if not flag and nums[i] == target:
            startIndex = i
            flag = True
        elif nums[i] == target:
            index = i
        if flag and nums[i] != target:
            break
        i += 1
    return [startIndex, index]
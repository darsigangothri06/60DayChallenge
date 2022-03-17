nums = [7,1,5,4]
i = 0
j = 1
Profit = 0
for j in range(len(nums)):
    if nums[i] > nums[j]:
        i = j
    else:
        Profit = max(Profit, nums[j] - nums[i])
if(Profit):
    return Profit
return -1
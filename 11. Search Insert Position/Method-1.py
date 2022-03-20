nums = [1,3,5,6]
target = 5
low = 0
high = len(nums)
while high > low:
    mid = (low + high)//2
    if nums[mid] > target:
        high = mid
    elif nums[mid] < target:
        low = mid + 1
    elif target == nums[mid]:
        return mid
return low
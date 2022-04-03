nums = [1,2,3]
# Step 1 - Finding the position
i = len(nums) - 2
while(i >= 0 and nums[i] >= nums[i+1]):
    i -= 1
# Step 2 - Finding the number that we need to substitute
if i>= 0:
    j = len(nums) - 1
    while(j >= 0 and nums[j] <= nums[i]):
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
# Step 3 - Reversing the remaining array - Sorting in ascending order
start = i + 1
end = len(nums) - 1
while(start < end):
    nums[start], nums[end] = nums[end], nums[start]
    start += 1
    end -= 1    
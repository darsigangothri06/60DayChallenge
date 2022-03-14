nums = [1,2,3,4,5,6,7]
k = 3
k = k % len(nums)
L = nums[:len(nums) - k]
del nums[:len(nums) - k]
for i in L:
    nums.append(i)
print(nums)
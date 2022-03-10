nums = [-1,0,1,2,-1,-4]
nums.sort()
req = []
for i in range(len(nums) - 2):
    start = i + 1
    end = len(nums) - 1
    while(start < end):
        Sum = nums[i] + nums[start] + nums[end]
        if(Sum == 0):
            req.append([nums[i],nums[start],nums[end]])
            start += 1
            end -= 1
        elif(Sum > 0):
            end -= 1
        else:
            start += 1
print(req)
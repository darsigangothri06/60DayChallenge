nums = [0,1,2,2,3,0,4,2]
val = 2
if not nums:
    return 0
p = [i for i in nums if i != val]
nums[:len(p)] = p
return len(p)
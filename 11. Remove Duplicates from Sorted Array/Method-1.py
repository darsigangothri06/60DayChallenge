nums = [0,0,1,1,1,2,2,3,3,4]
p = sorted(set(nums))
nums[:len(p)] = p
print(len(p))
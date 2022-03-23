nums = [2,3,-2,4]
intial = maxProd = minProd = nums[0]
for n in nums[1:]:
    compare = [n, maxProd*n, minProd*n]
    maxProd = max(compare)
    minProd = min(compare)
    intial = max(intial, maxProd)
return intial
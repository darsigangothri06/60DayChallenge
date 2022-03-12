# 78. Subsets

nums = [1,2,3]
output = [[]]
for i in nums:
    output += [x + [i] for x in output]
print(output)
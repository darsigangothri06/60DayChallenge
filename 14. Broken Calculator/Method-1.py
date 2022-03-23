startValue = 2
target = 3
ans = 0
while startValue < target: ans, target = ans + 1 + target % 2, (target + target % 2) // 2
return ans + (startValue - target)
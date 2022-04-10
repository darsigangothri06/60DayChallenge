nums = list(map(int, str(num)))
even = sorted([i for i in nums if i % 2 == 0])
odd = sorted([i for i in nums if i % 2 != 0])
res = 0
for i in nums:
    if i % 2 == 0:
        res = res * 10 + even.pop()
    else:
        res = res * 10 + odd.pop()
return res
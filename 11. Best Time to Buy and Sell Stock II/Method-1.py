prices = [7,1,5,3,6,4]
i = 1
Sum = 0
while i < len(prices):
    if prices[i] > prices[i-1]:
        Sum += prices[i] - prices[i-1]
    i += 1
print(Sum)
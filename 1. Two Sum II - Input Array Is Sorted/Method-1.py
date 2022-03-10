numbers = [2,7,11,15]
target = 9
start = 0
end = len(numbers) - 1
while start < end:
    if(numbers[start] + numbers[end] > target):
        end = end - 1
    elif(numbers[start] + numbers[end] < target):
        start += 1
    else:
        print([start,end])
        break
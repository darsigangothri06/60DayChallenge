noOfSubStrings = [1 for i in range(5)]
if n == 1:
    return sum(noOfSubStrings)
for turn in range(2, n + 1):
    noOfSubStrings[0] = sum(noOfSubStrings)
    noOfSubStrings[1] = sum(noOfSubStrings[1:])
    noOfSubStrings[2] = sum(noOfSubStrings[2:])
    noOfSubStrings[3] = sum(noOfSubStrings[3:])
return sum(noOfSubStrings)
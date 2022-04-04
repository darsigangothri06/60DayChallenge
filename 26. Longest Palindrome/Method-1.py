palLength = 0
frequency = [s.count(i) for i in set(s)]
for i in frequency:
    if i % 2 == 0:
        palLength += i
    else:
        if palLength % 2 ==  0:
            palLength += i
        else:
            palLength += i - 1
return palLength
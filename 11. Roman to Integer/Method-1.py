s = "III"
Map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
Sum = 0
i = 0
for i in range(len(s)):
    if i + 1 < len(s) and Map[s[i]] < Map[s[i+1]]:
        Sum -= Map[s[i]]
    else:
        Sum += Map[s[i]]
print(Sum)
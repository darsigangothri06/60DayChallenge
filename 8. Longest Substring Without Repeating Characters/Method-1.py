s = "abcabcbb"
if not s:
    return 0
subString = s[0]
MaxLen = 1
for i in range(1,len(s)):
    if s[i] in subString:
        MaxLen = max(MaxLen, len(subString))
        subString = subString[subString.find(s[i])+1:] + s[i]
        MaxLen = max(MaxLen, len(subString))
        
    else:
        subString += s[i]
MaxLen = max(MaxLen, len(subString))
print(MaxLen)
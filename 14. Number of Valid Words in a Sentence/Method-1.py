sentence = "cat and  dog"
def Validate(s):
    if '-' in s:
        if s.count('-') != 1:
            return 0
        ind = s.find('-')
        if ind == 0 or ind+1 >= len(s) or not s[ind-1].islower() or not s[ind+1].islower():
            return 0
    for i in range(len(s)):
        if s[i] in ['!', '.',','] and i != len(s)-1:
                return 0
        if s[i].isdigit():
            return 0
    return 1
count = 0
for i in sentence.split():
    count += Validate(i)
return(count)
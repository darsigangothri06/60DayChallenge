res = 0
flag = False
sign = '+'
digit = False
for i in s:
    if not digit and not flag and (i == "-" or i == "+"):
        digit = True
        flag = True
        sign = i
    elif i == ' ' and not digit:
        continue
    elif not(i >= '0' and i <= '9'):
        break
    else:
        digit = True
        res = res * 10 + int(i)
    
if sign == "-":
    res = -res
if(res >= -2**31 and res <= (2**31 - 1)):
    return res
if res <= -2**31:
    return -2**31
return 2**31 - 1
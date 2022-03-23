if numRows == 1 or numRows >= len(s):
    return s
row, step = 0, 0
res = [''] * len(s) 
for c in s:
    res[row] += c
    if row == 0:
        step = 1
    elif row == numRows - 1:
        step = -1
    row += step
return "".join(res)
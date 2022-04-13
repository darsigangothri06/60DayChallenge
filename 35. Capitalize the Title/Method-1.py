words = title.split()
res = []
for i in words:
    if len(i) <= 2:
        res.append(i.lower())
    else:
        res.append(i[0].upper() + i[1:].lower())
return ' '.join(res)
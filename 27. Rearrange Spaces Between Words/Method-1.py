count = text.count(' ')
words = text.split()
if count == 0:
    return text
if len(words) > 1:
    chk = count//(len(words)-1)
    rem = count % (len(words)-1)
else:
    chk = 0
    rem = count
return (' ' * chk).join(words) + ' ' * rem
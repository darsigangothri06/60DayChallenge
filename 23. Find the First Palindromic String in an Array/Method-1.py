for i in words:
    if i == ''.join(reversed(i)):
        return i
return ""
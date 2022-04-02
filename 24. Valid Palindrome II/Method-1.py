if s == s[::-1]:
    return True
start = 0
end = len(s) - 1
while start < end:
    if s[start] != s[end]:
        remLeft = s[start + 1: end + 1]
        remRight = s[start : end]
        if remLeft == remLeft[::-1] or remRight == remRight[::-1]:
            return True
        return False
    start += 1
    end -= 1
return True
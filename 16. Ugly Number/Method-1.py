def Rec(n):
    if n < 1:
        return False
    if n == 1:
        return True
    elif n % 5 == 0:
        return Rec(n//5)
    elif n % 3 == 0:
        return Rec(n//3)
    elif n % 2 == 0:
        return Rec(n//2)
    return False
return Rec(n)
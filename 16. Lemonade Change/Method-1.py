five = 0
ten = 0 
twenty = 0
for i in range(len(bills)):
    if bills[i] == 5:
        five += 1
    elif bills[i] == 10:
        ten += 1
        five -= 1
    elif bills[i] == 20:
        if ten > 0 :
            five -= 1
            ten -= 1
        else:
            five -= 3
        twenty += 1
    if five < 0 or ten < 0 or twenty <0:
        return False
return True
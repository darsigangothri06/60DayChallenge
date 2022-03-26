words = ["pay","attention","practice","attend"]
pref = "at"
cnt = 0
for i in words:
    if 0 == i.find(pref):
        cnt += 1
return cnt
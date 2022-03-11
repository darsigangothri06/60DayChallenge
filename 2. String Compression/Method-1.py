# 443. String Compression
chars = ["a","a","b","b","c","c","c"]
cnt = 1
res = []
i = 0
for j in range(1,len(chars)):
    if(chars[i] == chars[j]):
        cnt += 1
    else:
        if cnt == 1:
            res += chars[i]
        else:
            res += chars[i] + str(cnt)
            print(res)
        i = j
        cnt = 1
if cnt == 1:
    res += chars[i]
else:
    res += chars[i] + str(cnt)
chars[:] = res
print(len(res))
cnt = 0
for i in range(1,num+1):
    if sum(map(int,str(i))) % 2 == 0:
        cnt += 1
return cnt
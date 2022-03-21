s = "ababcbacadefegdehijhklij"
maxInd = {}
res = []

for i in range(len(s)):
    maxInd[s[i]] = i
    
start, end = 0, maxInd[s[0]]
for i in range(len(s)):
    end = max(end, maxInd[s[i]])
    if i == end:
        res.append(end - start + 1)
        start = end + 1
print(res)
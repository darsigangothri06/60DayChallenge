s = "aaabb"
k = 3
if len(s) == 0:
    print(0)
count = collections.Counter(s)
for i in count:
    if count[i] < k:
        print(max(self.longestSubstring(p,k) for p in s.split(i)))
print(len(s))
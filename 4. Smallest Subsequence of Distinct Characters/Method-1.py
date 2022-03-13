s = "bcabc"
freq,stack={},[]
for char in set(s):
    freq[char]=s.count(char)
for char in s:
    if char in stack:
        freq[char]-=1
        continue
    while stack and stack[-1]>char and freq[stack[-1]]>0:
        stack.pop()
    stack.append(char)
    freq[char]-=1
print("".join(stack))
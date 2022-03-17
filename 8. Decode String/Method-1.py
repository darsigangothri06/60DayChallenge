s = "3[a]2[bc]"
stack = []
for i in s:
    if i != ']':
        stack.append(i)
    else:
        subString = ""
        while stack[-1] != '[':
            subString = stack.pop() + subString
        stack.pop() # '['
        k = ''
        while stack != [] and stack[-1].isdigit():
            k = stack.pop() + k
        stack.append(int(k) * subString)
print(''.join(stack))
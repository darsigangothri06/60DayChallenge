sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Max = 0
for i in sentences:
    Max = max(Max,len(i.split()))
return Max
sentence = "i love eating burger"
searchWord = "burg"
words = sentence.split()
for i in range(len(words)):
    if 0 == words[i].find(searchWord):
        return i+1
return -1
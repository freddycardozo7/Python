#Given a string s and an array of strings words of the same length.
#Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, 
#in any order, and without any intervening characters.

words=input("Enter list of words seperated by space : ").split(" ")
s= input("Enter the word:")
wordsize = len(words[0])
wordlength = wordsize * len(words)
outputIndex = []
tempArr = []
for i in range(len(s)-wordlength+1):
    # Store a temp word array
    tempWords = words[:]
    #if i + wordlength -1 < len(s):
    startIndex = i
    endIndex = startIndex + wordsize
    for t in range(len(words)):
        if s[startIndex:endIndex] in tempWords:
            tempWords.remove(s[startIndex:endIndex])
        startIndex+=wordsize
        endIndex+=wordsize

    if not tempWords:

        outputIndex.append(i)

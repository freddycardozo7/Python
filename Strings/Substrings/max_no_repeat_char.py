# Python program to find the longest substring  without repeating characters in a string
s = input("Enter the String")
maxstr = ''
substr = ''
for i in range(len(s)):
    #If character not in substring 
    if s[i] not in substr:
        if maxstr == substr:
            maxstr += s[i]
        substr += s[i]
    else:
        #If character is in  substring
        # Find the Index 
        indexFound = substr.index(s[i])
        
        # If indexFound is end of substring the start the substring from the end +2
        if indexFound == len(substr)-1:
            substr=s[i]
            
        # If Index is found at the start of substring the start the substring from the index found +1
        #elif indexFound == 0:
        #    substr = substr[1:]
        #    substr += s[i]
        else:
            substr = substr[indexFound+1:]
            substr += s[i]
        
        
    if len(substr) > len(maxstr):
        maxstr= substr
 
 print(

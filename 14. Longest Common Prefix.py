strs = []

if not strs:
    print('')
shortest = min(strs, key=len) #find the shortest word
for i, ch in enumerate(shortest): #go through each character in the shortest word
    for other in strs: #go through each word in the list
        if other[i] != ch: # find the place where the character of the word is not the same as the shortest word
            shortest= shortest[:i] #slice up until that position
print(shortest)




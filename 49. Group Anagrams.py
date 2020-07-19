#Given an array of strings, group anagrams together.

#my attempt, not successful
result = []
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def isAnagram(word1, word2):
    hmap = {}
    for char in word1:
        if char in hmap:
            hmap[char] += 1
        else:
            hmap[char] = 1
    for char in word2:
        if char in hmap:
            hmap[char] -= 1
        else:
            hmap[char] = 1
    for k in hmap:
        if hmap[k] != 0:
            return False
    return True

for i in range(1,len(strs)):
    for j in range(len(strs)):
        if j == i:
            continue
        if isAnagram(strs[j], strs[i]) == True:
            result.append([strs[i],strs[j]])

print(result)

#%%
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

#intuition: for each word (assume each word only contains 26 alphabet characters and no space)
#if the words are anagram, after sorted they will be the same => think about it as
#they have the same 'key'.
hmap = {}

for st in strs: #loop through the strs
    key = ''.join(sorted(st)) #create a 'key' by sorting the word
    if key not in hmap: #if key is not in map
        hmap[key] = [st] #we create the value of that key by adding
                        # the word, not the key, as a value.
                       # We want to add it as a list, hence the bracket []
    else: #if key is in map
        hmap[key] += [st] #we add the word as the value of that key, in the form of a list

print(hmap.values())
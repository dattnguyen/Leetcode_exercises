# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.

#using dictionary
def findtheDifference(s, t):
    hmap = {}

    for char in s:
        hmap[char] = hmap.get(char,0) + 1
    for char in t:
        if char in hmap:
            hmap[char] -= 1
        else:
            hmap[char] = 1
    for k in hmap:
        if hmap[k] != 0:
            return print(k)

s = 'abcd'
t = 'acedb'
findtheDifference(s,t)
#%%

# use XOR
def findtheDiff (s,t):
    hash = 0
    for char in s+t: #the bitwise XOR will output 0 if it sees 2 similar characters
        hash ^= ord(char) #use ord() to get the unicode of the character
    return print(chr(hash)) #use chr to turn the unicode back to the character

s = 'abcdddbbcca'
t = 'cacbaabdbdcd'
findtheDiff(s,t)

#%%
print(7%10)
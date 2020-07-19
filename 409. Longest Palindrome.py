# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.

s = 'cccddd'
hmap = {}
for char in s:
    if char in hmap:
        hmap[char] += 1
    else:
        hmap[char] = 1
print(hmap)
result = 0
plus_one = 0
for i in hmap:
    if hmap[i] % 2 == 1 and hmap[i] > 2:
        result += (hmap[i] - 1)
        plus_one = 1
    elif hmap[i] % 2 == 1 and hmap[i] == 1:
        plus_one = 1
    else:
        result += hmap[i]

print(result + plus_one)
#%%
#hash set approach
s = 'abccccdd'
hash = set()
result = 0

for char in s:
    if char not in hash:
        hash.add(char)
    else:
        hash.remove(char)
    # by add and then remove, hash only contain characters that appear odd times
    # or only ONE time, to be precise
#print(hash)

if len(hash) > 0:
    result = len(s) - len(hash) + 1 #remove character that appears one time and then +1
else:
    result = len(s)
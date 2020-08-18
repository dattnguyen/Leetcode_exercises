# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of
# both strings s and p will not be larger than 20,100.
# The order of output does not matter.

#brute force
s = 'tbcwebcdacbercab'
p = 'abc'

left = 0
right = len(p)
result = []
while right <= len(s):
    a = sorted(s[left:right])
    b = sorted(p)
    if a == b:
        result.append(left)
    left += 1
    right += 1

print(result)

#%%

#2 dictionary
from collections import Counter
s = 'abcdebca'
p = 'abc'
count_p = Counter(p)
count_s = Counter()

res = []

right = 0

for right in range(len(s)):
    count_s[s[right]] += 1
    if right >= len(p):
        if count_s[s[right-len(p)]] == 1: #if the frequency is
            del count_s[s[right-len(p)]]
        else:
            count_s[s[right-len(p)]] -= 1
    if count_s == count_p:
        res.append(right-len(p)+1)

print(res)
#%%
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        freq = [0] * 128
        for c in p:
            freq[ord(c)] += 1
        i,counter = 0,0;
        for j in range(0, len(s)):
            if freq[ord(s[j])] > 0 :
                counter += 1
            freq[ord(s[j])] -= 1
            if counter == len(p) :
                res.append(i)
            if (j - i + 1) == len(p):
                freq[ord(s[i])] += 1
                if freq[ord(s[i])] > 0: counter -= 1
                i += 1
        return res
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
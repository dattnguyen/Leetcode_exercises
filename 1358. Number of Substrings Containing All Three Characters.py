# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
from collections import Counter

s = "abca"

res = 0
left = 0

count = Counter()

for right in range(len(s)):
    count[s[right]] += 1
    while len(count) == 3:  
        res += len(s) - right
        count[s[left]] -= 1
        if not count[s[left]]:
            del count[s[left]]
        left += 1

print(res)
#%%

def numberOfSubstrings(s):
    slow, fast, n = 0, -1, len(s)
    d = {'a': 0, 'b': 0, 'c': 0}
    res = 0

    while slow < n or fast < n:
        if min(d.values()) >= 1:
            d[s[slow]] -= 1
            slow += 1
        while min(d.values()) < 1:
            if fast < n - 1:
                fast += 1
                d[s[fast]] += 1
            else:
                return print(res)
        res += n - fast

numberOfSubstrings('abca')
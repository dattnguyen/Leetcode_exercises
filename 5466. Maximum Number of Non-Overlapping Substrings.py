s = "adefaddaccc"
subs = []

def findChar(s, char):
    left = 0
    right = 0
    for i in range(len(s)):
        while s[left] != char:
            left += 1
        if s[i] == char:
            right = i
    return s[left:right + 1]

for i in range(len(s)):
    for j in range(len(s)):
        if j < i:
            continue
        subs.append(s[i:j+1])

result = []
for word in subs:
    if len(word) == 1:
        result.append(findChar(s, word))

clear = []
for x in result:
    if x not in clear:
        clear.append(x)
print(clear)

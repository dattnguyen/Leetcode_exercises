# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.


def wordPattern(pattern, str):
    hmap = {}
    for i, char in enumerate(pattern):
        if char in hmap:
            hmap[char] += [i]
        else:
            hmap[char] = [i]

    hmap2 = {}
    for i, word in enumerate(str.split(' ')):
        if word in hmap2:
            hmap2[word] += [i]
        else:
            hmap2[word] = [i]

    if len(hmap) != len(hmap2):
        return print('False')
    for key1, key2 in zip(hmap, hmap2):
        if hmap[key1] != hmap2[key2]:
            return print ('False')
        else:
            return print('True')


pattern = 'jquery'
str = 'jquery'

wordPattern(pattern, str)

#%%

def wordPattern2(pattern, str):
    words = str.split(' ')
    hmap = {}
    if len(words) != len(pattern):
        return print('False')

    for i in range(len(pattern)):
        if pattern[i] in hmap:

            if hmap[pattern[i]] != words[i]:
                return print('False')
        else:
            if words[i] not in hmap.values():
                hmap[pattern[i]] = words[i]
            else:
                return print('False')

    return print('True')

wordPattern2('abaa','dog dog dog dog')
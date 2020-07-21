# Given a string, sort it in decreasing order based on the frequency of characters.

#brute force
s = 'Aabb'

hmap = {}

for char in s: #add all characters in a map
    if char not in hmap:
        hmap[char] = 1
    else:
        hmap[char] += 1

#sort the map based on value
hmap_sorted = sorted(hmap.items(), key = lambda x: x[1], reverse=True)

res = ''
for i, key in hmap_sorted:
    res += i*key #return value with append and join on an empty list
print(res)
# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1.

#intuition is: you want a hashmap to keep track of the index, and a seen set
#to keep track if the character already appears.
def firstUniqchar(s):
    hmap = {}
    seen = set() #Unordered collections of unique elements¶
    for i, char in enumerate(s):
        if char not in seen: #if you have not seen it, then you can add it to hashmap and the seen set
            hmap[char] = i
            seen.add(char)
        elif char in hmap: #if you seen it, and it is also in hashmap, then we delete it
            del hmap[char]

    return print(seen)

firstUniqchar('aadadaad')
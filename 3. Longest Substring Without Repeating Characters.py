# Given a string, find the length of the longest substring without repeating characters.

#slicing window - 2 pointer technique
def lengthofLongestSubstr(s):
    left = 0
    counter = 0

    for right in range(len(s)): #loop through the string
        if s[right] in s[left:right]: #if see repeating character
            while s[left] != s[right]: #move left pointer until you see the position of the repeated character
                left += 1
            counter = max (counter, right - left) #update the counter
            left += 1 #point to the position next to the first repeat character
        else:
            counter = max(counter, right - left + 1) #if no repeating character, update normally
    print(counter)

lengthofLongestSubstr('abcbadcablmn')
#%%
#use map to store characters:

s = "pwwkew"

hmap = {}
left = 0
result = 0

for i, char in enumerate(s):
    if char in hmap and left <= hmap[char]: #if see the repeated char, and we haven't gone over that position
        left = hmap[char] + 1 #move the left pointer to the next position
    else:
        result = max(result, i - left +1) #update the counter
    hmap[char] = i #add the character to the map if not repeated yet

print(result)
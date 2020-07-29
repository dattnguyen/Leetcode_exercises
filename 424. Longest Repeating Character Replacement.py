# Given a string s that consists of only uppercase English letters,
# you can perform at most k operations on that string.
# In one operation, you can choose any character of the string and
# change it to any other uppercase English character.
# Find the length of the longest sub-string containing
# all repeating letters you can get after performing the above operations.

#sliding window with hashmap to keep track
import collections
s = 'AAAAA'
k = 1
left = 0
counter = collections.Counter()
res = 0
for right in range(len(s)):
    counter[s[right]] += 1 #increase the frequency
    #print(counter)
    while (right-left+1) - max(counter.values()) > k:
        #first part is the length of window
        #second part the most frequent character
        #the difference the time we can tolerate

        counter[s[left]] -=1 #if we can't tolerate, we STILL move the window forward
        left += 1 #but we take out the character at the tail
    res = max(res, right-left+1) #we need this in case the whole string is valid

print(res)
#%%
s = 'AABABBA'
k = 1
count = collections.Counter()
res = 0

for i in range(len(s)):
    count[s[i]] += 1
    if res - max(count.values()) < k: #similar idea but not using a while loop
        res += 1 #when the condition is met, keep increasing the size of the window
    else:
        count[s[i - res]] -= 1 #take out the character at the tail
print(res)
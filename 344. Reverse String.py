# #Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

s = ["H","a","n","n","a","h"]

head = 0
tail = len(s)-1

while head < tail: #2 pointer technique
    s[head], s[tail] = s[tail], s[head]
    head += 1
    tail -= 1

print(s)
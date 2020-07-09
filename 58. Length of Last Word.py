# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word (last word means the last appearing word if we loop from left to right)
# in the string. If the last word does not exist, return 0.
# Note: A word is defined as a maximal substring consisting of non-space characters only.

def lengthofLastWord (s):
    count = 0
    local_count = 0 #you need a local count for the scenario where there is a space at the end
    for char in s:
        if char != ' ':
            local_count +=1
            count = local_count #if there is a space, the count doesn't get reset
        else:
            local_count = 0
    return print(count)

lengthofLastWord('hello is this me ')

#%%
def lengthofLastWord (s):
    return len(s.rstrip(' ').split(' ')[-1])

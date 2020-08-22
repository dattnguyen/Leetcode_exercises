# A string S of lowercase English letters is given.
# We want to partition this string into as many parts as possible
# so that each letter appears in at most one part,
# and return a list of integers representing the size of these parts.

#intuition is: find the first and last indices of each character
#result is a list of intervals of each character
#if we see an overlap, we merge them, and calculate the difference

#create a merge function, similar to problem 56

def partitionLabels(S):
    # merge intervals
    def merge(intervals):
        #no need base case and sort here
        stack = [intervals[0]]

        for x in intervals[1:]:
            if stack[-1][1] >= x[0]:
                stack[-1][1] = max(stack[-1][1], x[1])
            else:
                stack.append(x)

        #instead of returning list of list, we return list of list size
        res = [j[1] - j[0] + 1 for j in stack]

        return res

    # find first and last indices of each character:

    hmap = {}

    for i, char in enumerate(S):
        if char in hmap:
            hmap[char] = [hmap[char][0], i]
        else:
            hmap[char] = [i, i]

    return print(merge([hmap[k] for k in hmap]))

partitionLabels('ababcbacadefegdehijhklij')

#%%
#two pointer technique

# create a 'rightmost' hashmap:

#{'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# a b a b c b a c a  d  e  f  e  g  d  e  h  i  j  h  k  l  i
# |________________| everytime you see a character 'a', you want to 'expand'
# the window to capture the last character 'a' in the string
# we use the right most hashmap to do that


#left and right pointer. Pointer right will check if the current index
#is equal to the rightmost index of that char

def partition_twopt(S):
    rightmost = {c:i for i,c in enumerate(S)}
    left = 0
    right = 0
    res = []
    for i, char in enumerate(S):
        right = max(right, rightmost[char]) #find the furtherest character that
                                            #our window needs to capture
        # print(right)
        if i == right: #we know that we don't need to expand our window
            res += [right-left+1] #calculate the length of the window
            left = i + 1 #move left up one to start a new partition
    return print(res)
partition_twopt('ababcbacadefegdehijhklij')

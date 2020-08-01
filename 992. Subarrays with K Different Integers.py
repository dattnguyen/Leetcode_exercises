# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if
# the number of different integers in that subarray is exactly K.
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
# Return the number of good subarrays of A.

#NOT DONE
#my failed attempt
from collections import Counter

A = [1,2,1,2,3]

k = 2
temp = k
res = 0

for left in range(len(A)):
    hmap = Counter()
    for right in range(left,len(A)):

        if A[right] not in hmap:
            hmap[A[right]] = 1
            k -= 1
        else:
            hmap[A[right]] += 1

        while len(hmap) <= temp:
            res += 1
            hmap[A[left]] -= 1
            if hmap[A[left]] == 0:
                del hmap[A[left]]
                k += 1
            left += 1
print(res)

#%%

#the idea is that 'exactly K' = 'at most K' - 'at most K-1'
#first, we find number of substrings with at most K distinct character

def findatMostK(A, k):
    counter = Counter()
    left = res = 0
    for right in range(len(A)):
        if counter[A[right]] == 0: #if the character is not in there
            k -= 1 #reduce k by 1, we find the 1 distinct character
        counter[A[right]] += 1 #otherwise, we increase character's frequency
        while k < 0: #when we violate the condition
            counter[A[left]] -= 1 #we're going to move left pointer, but first
                                #we need to update its frequency in the map
            if counter[A[left]] == 0: #if we reduce the frequency to 0, meaning
                                #the character is not in the substring anymore
                k += 1 #we increase k, because we now have more distinct character to find
            left += 1 #move the left pointer
        res += right - left + 1 #see explanation below
    return res
# findatMostK([1,2,1,2,3], 2)

def subarraysWithKDistinct(A, K):
    return print(findatMostK(A,K)-findatMostK(A,K))

subarraysWithKDistinct([1,2,1,2,3],2)
#why would you increase the result by the length of the window (res += right - left + 1)
#[1,2,1,2] will produce a total of 10 different contiguous subarrays:

# [1,2,1,2] (1 different contiguous subarrays with length 4)
# [1,2,1], [2,1,2] (2 different contiguous subarrays with length 3)
# [1, 2], [1,2], [2,1](3 different contiguous subarrays with length 2)
# [1], [2], [1], [2] (4 different contiguous subarrays with length 1)

#by moving the left pointer forward, you remove the 1. We will lose 4 arrays: [1,2,1,2],
# [1,2,1], [1, 2], and [1]. Similarly when you keep moving the left pointer, you will remove 2.
# and you remove 3 arrays: [2,1,2], [1,2], [2]
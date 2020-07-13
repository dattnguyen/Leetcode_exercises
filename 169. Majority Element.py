# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

def majorityElement(nums):
    hmap = {}
    for i in nums: #count the frequency with dictionary/hashmap
        if i in hmap:
            hmap[i] += 1
        else:
            hmap[i] = 1
    for i in hmap: #find the one with highest frequency, O(2n) time complexity
        if hmap[i] > (len(nums)/2):
            return print(i)

#%%
#Boyer-Moore Majority Vote Algorithm

def majorityElement2(nums): # O(n)
    major = nums[0]
    counter = 0
    for i in nums:
        if counter == 0: #if the counter is 0, we set the current cendidate to i, and increase counter
            counter += 1
            major = i
        elif major == i: #in case the candidate is already there, we also increase the counter
            counter += 1
        else: #if the counter is not 0, and the pointer i is NOT the current candidate, then we decrease the counter
            counter -= 1
    return print(major)

majorityElement2([4,4,5,2,4])
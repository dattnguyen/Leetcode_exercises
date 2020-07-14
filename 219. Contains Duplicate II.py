# Given an array of integers and an integer k, find out whether there are two distinct
# indices i and j in the array such that nums[i] = nums[j]
# and the absolute difference between i and j is at most k.

def containsNearbyDuplicate (nums, k):

    dict = {}
    for i, num in enumerate(nums):
        if num in dict and i - dict[num] <=k:
            return print('True')
        dict[num] = i
    return print('False')
containsNearbyDuplicate([1,0,1,1], 1)
#%%
#why is this not working? question is confusing. This is a different approach
def containsNearbyDuplicate2 (nums, k):

    pointer = 0
    while pointer < len(nums):
        for i in range(pointer+1, len(nums)):
            if nums[i] == nums[pointer] and (i - pointer) > k:
                return print('False')
        pointer += 1
    return print('True')
containsNearbyDuplicate2([1,0,1,1], 1)
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.

def findmin(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high)//2
        if nums[mid] > nums[high]:
            low = mid + 1Find
        else:
            high = mid

    return print(nums[low])

findmin([15 ,17, 18, 20, 1, 2, 5, 7, 8, 11, 13])
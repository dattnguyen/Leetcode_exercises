# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.

nums = [2]

#sequential search
def findPeakElement(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return print(i-1)
    return print(len(nums)-1)

#findPeakElement([1,2,4,6,3,4,7,9,0,1])

#%%
#binary search iteration

def findPeakElement2(nums):
    left = 0
    right = len(nums)-1
    while left+1 < right:
        mid = (left + right)//2
        #print(mid)
        if nums[mid] < nums[mid-1]:
            right = mid - 1
        else:
            left = mid
    if nums[left] < nums[right]:
        return print(nums[right])
    else:
        return print(nums[left])
findPeakElement2([1,2,4,6,3,4,7,9,0,1])

#%%
#binary search recursion

#imagine the array as a range of mountains with different peaks
#if the mid point is smaller than the next point, we know we're on the left side
#of the mountain, or we're going up, and the max is on the right side
#we pull the left index to mid + 1, because mid+1 is potentially the local max
def findPeakElement3(nums_big):

    def helper(nums, left, right):
        if left == right:
            return print(left)
        else:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return helper(nums,left, mid)
            else:
                return helper(nums,mid+1, right)

    return helper(nums_big,0,len(nums_big)-1)
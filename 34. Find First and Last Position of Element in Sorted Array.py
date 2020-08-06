# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1]

#1 binary search + 2 pointers to find left and right index, logn + n = O(n)
def searchRange(nums, target):
    low = 0
    high = len(nums) - 1
    res = []
    while low <= high: #find the target
        mid = (high+low)//2
        if nums[mid] == target:
            i = j = mid #2 pointer to find the left and right index of the window
            while nums[mid] == nums[i] and i >= 0:
                i -= 1
            res.append(i + 1)
            while nums[mid] == nums[j] and j < len(nums) - 1:
                j += 1
            if nums[j] == target:
                res.append(j)
            else:
                res.append(j - 1)
            return print(res)
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return print([-1,-1])
nums = [5,7,7,8,8,8,10,12]
target = 7
searchRange(nums,target)

#%%
#2 binary search

def searchRange_2binary(nums,target):
    def binary_left(nums,target):
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = (low+high) // 2

            # -----mid---target-------
            #if mid < target, we increase low by mid + 1
            #the next index will be the beginning of the target window
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def binary_right(nums,target):
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = (low+high) // 2

            # -----target---mid-------
            # similarly if mid > target, we decrease high by mid - 1
            # the next index will be the end of the target window
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return high

    left, right = binary_left(nums,target), binary_right(nums,target)

    return print(left,right) if left <= right else print([-1,-1])

searchRange_2binary([1,8,8,8,8,8,8], 8)
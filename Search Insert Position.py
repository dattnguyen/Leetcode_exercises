#Given a sorted array and a target value, return the index if the target is found.
#If not, return the index where it would be if it were inserted in order.
#You may assume no duplicates in the array.

nums = [4, 6, 7, 9, 10, 23]
target = 12

# for i in range(0, len(nums)):
#     if target >
if target > max(nums):
    print(len(nums))
elif target < nums[0]:
    print (0)
for i in range(len(nums)):
    if target == nums[i]:
        print(i)
    elif target > nums[i] and target < nums[i+1]:
        print(i+1)

#%%
#binary search
nums = [4, 6, 7, 9, 10, 14, 16, 20]

def searchpos (nums, target):
    low = 0 #lower bound is the very first index
    high = len(nums) - 1 #upper bound is the length of the string, subtract one because of index 0
    while low <= high:
        mid = int((low + high)/2) #look at the mid position
        if nums[mid] == target: #if target is at mid position, great
            return print(mid)
        elif nums[mid] < target: #if middle position is LESS than target
            low = mid +1    #we need to increase the low end, so that the new 'mid' would look at a higher position number
                            # or
        else:
            high = mid - 1  #we need to look reduce the higher bound if the middle position is larger than the target
    return print(low)

searchpos (nums, 9)


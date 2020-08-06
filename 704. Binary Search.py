# Given a sorted (in ascending order) integer array nums of n elements and a target value,
# write a function to search target in nums. If target exists, then return its index,
# otherwise return -1.

def search(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        middle = (left+right)//2
        if nums[middle] == target:
            return print(middle)

        elif nums[middle] < target:
            left = middle + 1

        else:
            right = middle - 1
    return -1

search([5,7,7,8,8,8,10,12],8)
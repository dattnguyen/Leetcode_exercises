#Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

#create another array, use O(n) time and O(n) space
nums = [0,1,0,3,12]

result = []
counter = 0
for i  in nums:
    if i != 0:
        result.append(i)
    else:
        counter += 1
for i in range(counter):
    result.append(0)

print(result)
#%%
#two pointer technique

def moveZeroes(nums):
    right = 0
    left = 0
    while right < len(nums):
        if nums[right] == 0: #if the right pointer sees a zero, we increment it
            right += 1
        else: #until the right pointer see a non-zero
            nums[left], nums[right] = nums[right], nums[left] #we swap right and left
            right += 1 #and then increment both pointers
            left += 1
    return print(nums)

moveZeroes([0,0,1,0,3,12])
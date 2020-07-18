# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

nums = [-1, 0, 1, 2, -1, -4]

hmap = {}
res = []

for i in range(len(nums)):
    target = 0 - nums[i]
    for j, num in enumerate(nums):
        if j != i:
            temp = target - num
            if temp not in hmap:
                hmap[num] = 1
            else:
                res.append([num, temp, nums[i]])

print(res)
#%%
nums = [-1, 0, 1, 2, -1, -4]

#idea is a+b = -c => use 2Sum problem to solve 3Sum
#for duplicate case, we use continue to keep increasing i
#sort makes everything easier
nums.sort()
result = []
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]: #handle duplicate case
        continue
    target = 0 - nums[i] #turn this into 2Sum
    left = i+1
    right = len(nums)-1
    while left < right: #sort and then use 2 pointer technique to find a and b
        if nums[left] + nums[right] == target:
            result.append([nums[i], nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]: #handle duplicate case in 2Sum
                left +=1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1

print(result)
import math
nums = [-5, -2, -4, -5]

#Kadane's algo
local_max = 0
global_max = -math.inf

for i in range(len(nums)):
    local_max = max(nums[i], local_max + nums[i])

    global_max = max(global_max, local_max)

print(global_max)

#%%
nums = [-5, -2, -4, -5]
for i in range(1, len(nums)): #we use Kadane's algorithm by looking at the previous subarray
                            # and compare the max of (current index, sum of previous subarray)
    if nums[i - 1] > 0: #if the previous subarray is positive, it can get bigger so. This will save some time
        nums[i] += nums[i - 1]
print(max(nums))
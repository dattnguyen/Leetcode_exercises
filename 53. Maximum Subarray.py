nums = [-5, -2, -4, -5]
current_sum = 0
best_sum = 0
for i in nums:
    current_sum = max (0, current_sum+i)
    best_sum = max (best_sum, current_sum)
    print(best_sum)
print(best_sum)
#%%
nums =  [-5, -2, -4, -5]
for i in range(1, len(nums)): #we use Kadane's algorithm by looking at the previous subarray
                            # and compare the max of (current index, sum of previous subarray)
    if nums[i - 1] > 0: #if the previous subarray is positive, it can get bigger so. This will save some time
        nums[i] += nums[i - 1]
print(max(nums))
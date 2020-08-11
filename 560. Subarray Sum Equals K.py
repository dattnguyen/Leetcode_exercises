# Given an array of integers and an integer k, you need to find
# the total number of continuous subarrays whose sum equals to k.

nums = [3,4,7,2,-3,1,4,2,1]
k = 7

# prefix sum and a dictionary to keep track
# see https://www.youtube.com/watch?v=bqN9yB0vF08 for explanation
check = {0:1}
counter = 0
preSum = 0

#intuition is that the difference between presum[j] - presum[i]
#equal to the sum of the elements between index j and i
#instead of finding the difference between presum[j] and presum[i] that equal k
#we check if presum[j] - k = presum[i] by storing presum[i] in a dictionary
for num in nums:
    preSum += num
    if preSum - k in check:
        counter += check[preSum-k]
    if preSum in check:
        check[preSum] += 1
    else:
        check[preSum] =1

print(counter)

#%%
nums = [3,4,7,2,-3,1,4,2,1]
presum = []
total = 0
for i in range(len(nums)):
    total += nums[i]
    presum.append(total)

print(presum)
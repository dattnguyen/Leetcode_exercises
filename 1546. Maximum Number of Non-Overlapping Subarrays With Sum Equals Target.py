# Given an array nums and an integer target.
#
# Return the maximum number of non-empty non-overlapping subarrays
# such that the sum of values in each subarray is equal to target.

nums = [3,4,7,2,-3,1,4,2,1]
target = 7

#idea is whenever we see find a valid subarray, we reset our dictionary
#similar to two sum
hmap = {0:0}
presum = 0
res = 0
for num in nums:
    presum += num
    if presum - target in hmap:
        res += 1
        hmap = {}
    hmap[presum] = 1
print(res)
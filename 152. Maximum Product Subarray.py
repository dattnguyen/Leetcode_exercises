# Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
import math

#the idea is to store both the min and the max of the subarray. When you see a negative
#number, the min will become the max
nums = [-2,0,-3,-4,0,10]

imin = imax = 1
res = -math.inf
for i in range(len(nums)):
    if nums[i] < 0:
        imin, imax = imax, imin

    #print('imin = ', imin, 'imax = ', imax, 'max so far: ', res)

    imax = max(nums[i], imax * nums[i])
    imin = min(nums[i], imin * nums[i])

    res = max(res,imax)
    #print('imin = ', imin, 'imax = ', imax, 'max so far: ', res)

    #print('\n')

print (res)

#%%
A = [-2,0,-3,-4,0,10]

B = A[::-1]
for i in range(1, len(A)):
    A[i] *= A[i - 1] or 1
    B[i] *= B[i - 1] or 1
print (max(A + B))

#%%
nums = [-2,0,-3]
ans = -math.inf
prefix = suffix = 1
for i in range(len(nums)):
    prefix = (prefix or 1) * nums[i]
    suffix = (suffix or 1) * nums[~i]
    ans = max(ans, prefix, suffix)
print(ans)
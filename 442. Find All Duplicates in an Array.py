# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

nums = [4,3,2,7,8,2,3,1]

from collections import Counter
count = Counter()
res = []

for i,v in enumerate(nums):
    if v in count:
        count[v] += 1
        res.append(v)
    else:
        count[v] = 1

print(res)

#%%
#without extra space

#the catch here is that all elements in the array is positive (>=1)
#and smaller than the size of the array n
#we use the array itself to hash

nums = [4,3,2,7,8,2,3,1]
res = []

for num in nums: #if the number appears twice, it will hash the 'element' to negative the first time
                #we see the number then we can pick out that number when we see the 'element' again
    if nums[abs(num)-1] < 0:
        res.append(abs(num))
    else:
        nums[abs(num)-1] *= -1

print(nums)
#Given a non-empty array of integers, every element appears twice except for one.
# Find that single one.

nums = [4,1,2,1,2]

hmap = {}

for i, num in enumerate(nums):
    if num in hmap:
        hmap[num] += 1
    else:
        hmap[num] = 1

for num in hmap:
    if hmap[num] == 1:
        print(num)
#%%

# XOR approach

nums = [4,1,2,1,2]
result = 0

for n in nums:
    result ^= n

print(result)
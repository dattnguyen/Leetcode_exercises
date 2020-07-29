# Given two arrays, write a function to compute their intersection.
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
res = []
hmap = {}
for i in nums1:
    hmap[i] = hmap[i] + 1 if i in hmap else 1

for j in nums2:
    if j in hmap and hmap[j] >0: #or if j in hmap and j not in res
        res.append(j)
        hmap[j] = 0
print(res)

#%%
#binary search

def intersection(nums1,nums2):
    res = []
    nums2 = sorted(nums2)

    for num in nums1:
        left = 0
        right = len(nums2) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums2[mid] == num and num not in res:
                res.append(num)
            elif nums2[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
    return res
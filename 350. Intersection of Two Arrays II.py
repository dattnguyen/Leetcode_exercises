# # Given two arrays, write a function to compute their intersection.
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

def intersection(nums1, nums2):
    hmap1 = {}
    hmap2 = {}
    res = []
    for i in nums1:
        hmap1[i] = hmap1.get(i,0) +1
    for j in nums2:
        hmap2[j] = hmap2.get(i, 0) + 1

    for key1, value1 in hmap1:
        if key1 in hmap2:
            res.append([key1]*min(hmap1[key1],hmap2[key1]))

    return print(res)

intersection([4,9,5], [9,4,9,8,4])
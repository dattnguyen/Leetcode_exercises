# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

def merge(nums1, m, nums2, n): #we are sorting from right to left, filling as we go along
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]: #we compare the last largest element of nums1 with the largest element of nums2
            nums1[m + n - 1] = nums1[m - 1] #if it's greater, we push it to the last position
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0: #in the case that m is already get to 0 but there are still elements in the nums1
        nums1[:n] = nums2[:n] #we know that these elements will be less than the smallest value of nums1, we can just copy them over
    return print(nums1)
merge([3,3,4,0,0,0], 3, [1,1,8],3)
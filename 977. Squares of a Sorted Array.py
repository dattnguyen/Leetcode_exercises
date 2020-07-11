#Given an array of integers A sorted in non-decreasing order, return an array
#of the squares of each number, also in sorted non-decreasing order.

def sortedSquares(nums):

    nums1 = [x**2 for x in nums if x >= 0] #create 2 lists, one with positive numbers, one with negative
    nums2 = [x**2 for x in nums if x < 0]
    nums2 = nums2[::-1] #reverse the negative list

    #problem now becomes 'merge 2 sorted array
    m = len(nums1) #two pointer technique
    n = len(nums2)
    while m>0 and n>0:
        if nums1[m-1] > nums2[n-1]:
            nums[m+n-1] = nums1[m-1]
            m -=1
        else:
            nums[m+n-1] = nums2[n-1]
            n -=1
    if n > 0:
        nums[:n] = nums2[:n]
    if m > 0:
        nums[:m] = nums1[:m]

    return print(nums)

sortedSquares([-7,-2,-1,0, 2, 6])
#%%
def sortedSquares_2(nums):
    ans = [0] * len(nums) #create a placeholder list with enough space
    left = 0 # two pointer technique, going from left to right and right to left simultaneously and compare
    right = len(nums)-1
    while left <= right: # left and right will converge and we know we account for all elements

        if abs(nums[left]) > abs(nums[right]): #compare the largest numbers from two ends, then push it to the end of the list
            ans[right-left] = nums[left]**2
            left += 1
        else:
            ans[right-left] = nums[right]**2
            right -= 1
    return print(ans)

sortedSquares_2([-4,-1,0,3,10])

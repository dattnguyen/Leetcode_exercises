# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

def search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return print(mid)

        if nums[mid] < nums[right]: #if mid less than right, we know that everything from mid to right has been sorted

            if nums[mid] <= target <= nums[right]: #check if target is in this sorted part
                left = mid + 1 #if yes, bring the left to mid + 1 (because we already check mid)
            else:
                right = mid - 1 #if it's on the other section, bring right to mid -1
        else:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return (print(-1))
search([15 ,17, 18, 20, 1, 2, 5, 7, 8, 11, 13], 17)

#%%
#find the index of the smallest value

nums = [4,5,6,7,0,1,2]
n= len(nums)
target = 0
low = 0
high = n - 1

while low < high: # we find the min (see LC#33)
    mid = (low + high)//2
    if nums[mid] > nums[high]:
        low = mid + 1
    else:
        high = mid

#start the normal binary search
start = 0
end = n - 1
#print(left)

while start <= end:
    mid2 = (start+end)//2
    realmid = (mid2+low) % n #see below

    if nums[realmid] == target:
        print(realmid)
    if nums[realmid] < target:
        start = mid2 + 1
    else:
        end = mid2 - 1

# For those who struggled to figure out why it is realmid=(mid+rot)%n: you can think of it this way:
# If we want to find realmid for array [4,5,6,7,0,1,2], you can shift the part before the rotating point
# to the end of the array (after 2) so that the sorted array is "recovered" from the rotating point but only longer,
# like this: [4, 5, 6, 7, 0, 1, 2, 4, 5, 6, 7]. The real mid in this longer array is the middle point between
# the rotating point and the last element: (rot + (hi+rot)) / 2. (hi + rot) is the index of the last element.
# And of course, this result is larger than the real middle. So you just need to wrap around and
# get the remainder: ((rot + (hi + rot)) / 2) % n. And this expression is effectively (rot + hi/2) % n,
# which is (rot+mid) % n.
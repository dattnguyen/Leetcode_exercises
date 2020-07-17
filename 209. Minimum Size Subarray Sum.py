# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.

# nums = [2,3,1,2,4,3]
# s = 7

#the idea is that when we find a sub array that satisfies the condition, we want to
#remove the first element of the sub array to see if we can do better by keep going
#removing the old elements
def minSubArrayLen (s, nums):
    left = 0 # 2 pointer, 1 point at the beginning
    sub_sum = 0 #keep track of the sum of the sub array
    res = len(nums) + 1 #update the minimum length of array as we go

    for i in range(len(nums)): #loop through the array
        sub_sum += nums[i] #add in new element
        #print('i = ', i, 'sub sum ', sub_sum)
        while sub_sum >= s:
            res = min (res, i-left+1) #if we find the sub sum that satisfies condition
            sub_sum -= nums[left] #we shorten the sub array by the left index and move forward
            left += 1
    return print(res) if res <= len(nums) else print(0)

minSubArrayLen(8,[1,4,2,3,1,5,1,3])
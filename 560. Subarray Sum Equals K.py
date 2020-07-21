# Given an array of integers and an integer k, you need to find
# the total number of continuous subarrays whose sum equals to k.

nums = [3,4,7,2,-3,1,4,2,1]
k = 7

# prefix sum and a dictionary to keep track
# see https://www.youtube.com/watch?v=bqN9yB0vF08 for explanation
check = {0:1}
counter = 0
preSum = 0

for num in nums:
    preSum += num
    if preSum - k in check:
        counter += check[preSum-k]
    if preSum in check:
        check[preSum] += 1
    else:
        check[preSum] =1

print(counter)
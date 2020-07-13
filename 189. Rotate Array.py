# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

#the idea is if we rotate k times ,the last k elements will move to the front, and the rest
#from the front shift to the end. You can either reverse all elements first, then reverse
#the first k elements followed by reversing the rest (n-k) elements

def reverse(nums, head, tail): #create a reverse function
    while head < tail:
        nums[head], nums[tail] = nums[tail], nums[head]
        head, tail = head+1, tail-1
    return nums

def reversek(nums, k):

    n = len(nums)
    nums = reverse(nums, 0, n-k-1) #reverse the first (n-k) element
    nums = reverse(nums, n-k, n-1)  #reverse the last k element
    nums = reverse(nums, 0, n-1) #reverse the whole thing

    return print(nums)

reversek([1,2,3,4,5,6,7,8], k)

#%%
#brute force
nums = [1,2,3,4,5,6,7,8]
k = 3

k %= len(nums) #optimization: if there are 7 elements, and you shift it 7 times, the array won't change

for i in range(k): #shift 1 element to the right, do it k times
    previous = nums[-1] #store the last element
    for j in range(len(nums)): #swap the elements
        nums[j], previous = previous, nums[j]

print(nums)

#%%
# Cyclic replacements
nums = [1,2,3,4,5,6,7,8]
n = len(nums)
k = 3
k %= n

start = count = 0
while count < n:
    current, prev = start, nums[start]
    while True:
        next_idx = (current + k) % n
        nums[next_idx], prev = prev, nums[next_idx]
        current = next_idx
        count += 1

        if start == current:
            break
    start += 1

print(nums)

nums = [3,2,2,3]
val = 3

head = 0

for i in range(0, len(nums)):
    if nums[i] != val:
        nums[head] = nums[i]
        head += 1
print(nums)
#%%
nums = [3,2,2,3]
val = 3
start = 0 #the idea is swapping the element to the end of the array if it equals to the value
end = len(nums) - 1 #we go from left to right for our 'start' and right to left for our 'end'
while start <= end: #when start reach end, we know that the rest are just the value
    if nums[start] == val:
        nums[start] = nums[end]
        nums[end] = nums[start]
        end = end - 1 #we need this to move to the element next to the end value
    else:
        start += 1
print(nums)

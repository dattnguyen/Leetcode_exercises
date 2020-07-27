#%% brute force
def twoSum(nums,target):
    plist = []
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if i !=j and nums[i]+ nums[j] == target and i not in plist and j not in plist:
                plist.append(i)
                plist.append(j)
    return print(plist)
mylist = [2, 7, 11, 15, 22, 67]
target = 69
twoSum(mylist, target)
#%%
def twoSum(mylist, target):
    h = {} #create a hash table to store the values and the indices or positions
    for i, num in enumerate(mylist):
        n = target - num #the sum has 2 components. We look for the other components
        if n not in h:
            h[num] = i
            #print(h)
        else:
            print ([h[n], i])
mylist = [2, 7, 11, 15, 22, 67]
target = 24
twoSum(mylist,target)

#%%
#sorting and use 2 pointer technique
nums = [-1, 0, 1, 2, -1, -4, 3, 4, 7, 8, -2, 2]
target = 5

nums.sort() #sort the array first to use 2 pointer technique
left = 0
right = len(nums)-1
result = []

while left < right: #start from the two ends towards the middle
    if nums[left] + nums[right] == target:
        result.append([nums[left], nums[right]])
        left += 1
        while left < right and nums[left] == nums[left-1]: #account for duplicate
            # you still need left < right in the case [2,2,2,2], target = 4 otherwise out of index
            left += 1 #by moving the left pointer pass the duplicate value
    elif nums[left] + nums[right] > target: #if the sum is more than target, reduce right
        right -= 1
    else: #if the sum is less than target, increase left
        left += 1
print(result)
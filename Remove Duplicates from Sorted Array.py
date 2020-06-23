nums = [2, 4, 5, 5, 6, 6, 7, 8, 8]
mlist =[]
for x in nums:
    if x not in mlist:
        mlist.append(x)
nums = mlist
print(nums)
#%%
def removeDuplicates(): #the problem is asking if an array is already sorted
    head = 0 # create a starting point
    for x in range(1, len(nums)): # start with the second index position to compare
        if nums[x] != nums[head]: # if the second is different from the first
            head += 1 #increase the counter to compare the next position
            nums[head] = nums[x] #with the starting position is now updated to the second position
    return print(head+1)
nums = [2, 4, 5, 5, 6, 6, 7, 8, 8]
removeDuplicates()

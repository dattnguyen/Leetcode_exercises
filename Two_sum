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

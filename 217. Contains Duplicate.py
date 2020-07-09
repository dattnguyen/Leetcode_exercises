def containsDuplicate (nums):
    disc = []
    for x in nums:
        if x not in disc:
            disc.append(x)
    if len(disc) == len(nums):
        return print('False')
    else:
        return print('True')

containsDuplicate([1,1,1,3,3,4,3,2,4,2])

#%%
def containsDuplicate (nums):
    return print(len(nums) > len(set(nums)))

containsDuplicate([1,1,1,3,3,4,3,2,4,2])

#%%
nums = [1,1,1,3,3,4,3,2,4,2]
print (set(nums))
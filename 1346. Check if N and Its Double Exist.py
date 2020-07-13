# Given an array arr of integers, check if there exists two integers N and M such that
# N is the double of M ( i.e. N = 2 * M).

nums = [10,3,5,7,8,12]

def checkifexist(nums):
    hmap = {}

    for i in nums:
        if i not in hmap:
            hmap[i*2] = 1
            hmap[i/2] = 1
        else:
            return print('True')
    return print('False')

checkifexist([3,1,7,11])
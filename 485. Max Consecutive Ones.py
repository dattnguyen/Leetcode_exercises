#Given a binary array, find the maximum number of consecutive 1s in this array.

def findMaxconsecutiveOnes(nums):
    counter = 0 #have a counter, reset to 0 if it's not "one"
    max_count = 0 #keep track of the max count
    for i in range(len(nums)):
        if nums[i] == 1:
            counter += 1
            max_count = max(max_count, counter)
        else:
            counter = 0
    return print(max_count)

findMaxconsecutiveOnes([0,0,1,1,0,0,1,1,1,1,0,1])
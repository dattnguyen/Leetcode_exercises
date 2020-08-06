# Given a sorted array arr, two integers k and x, find the k closest elements to x
# in the array. The result should also be sorted in ascending order.
# If there is a tie, the smaller elements are always preferred.

#brute force, doesn't work
def findKClosest(arr, k, x):
    diff = {}
    res = []
    for num in arr:
        diff[num] = abs(x-num)

    sorted_map = {k: v for k, v in sorted(diff.items(), key=lambda item: item[1])}

    for key in sorted_map:
        res.append(key)
        k -=1
        if k == 0:
            return print(sorted(res))

findKClosest([0,1,1,1,2,3,6,7,8,9], 9, 4)

#%% O(n), 2 pointer

def findKClosest_2pointer(arr, k , x):
    low = 0
    high = len(arr)-1
    # res = []
    while high - low >= k: #the array is sorted so if we see that the distance from target
                        #between the low side is greater than left side, we shrink the low side
                        #and vice versa until we have enough k elements
        if x-arr[low] > arr[high]-x:
            low += 1
        else:
            high -= 1

    # for i in range(low, high+1): #add the elements to the list
    #     res.append(arr[i])

    return print(arr[low:high+1])

findKClosest_2pointer([0,2,4,6,8,10,12], 4, 6)

#%%
#binary search

def findKClosest_binary(arr, k, x):

    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high)//2
        if x - arr[mid] > arr[mid+k] -x:
            low = mid + 1
        else:
            high = mid

    return print(low, mid, high)

findKClosest_binary([1,3,5,6,9,10,12,15,17], 3, 6)

#%%
# [1,3,5,6,9,10,12,20,21]
arr= [0,1,2,4,5,5,7,9,10,12,14,16,17,20,22]
k = 4

x = 9
low = 0
high = len(arr)-k
while low < high:
    mid = (low+high)//2
    # print('low before is: ',low,'mid before is: ',mid,'high before is: ',high,)
    if x - arr[mid] > arr[mid+k] -x:
        low = mid + 1
    else:
        high = mid

    # print('low after is: ', low, 'mid after is: ', mid, 'high after is: ', high, )
print(arr[low: high+k])
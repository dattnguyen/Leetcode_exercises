# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

def minimumAbsDifference(arr):
    arr.sort() #sort the array first

    min_diff = abs(arr[0] - arr[1])
    for i in range(len(arr)): #find the min difference
        diff = abs(arr[i]-arr[i-1])
        min_diff = min(diff, min_diff)

    result = []
    for i in range(len(arr)): #find the pair that has the difference equal to the min difference
        if abs(arr[i-1] - arr[i]) == min_diff:
            result.append([arr[i-1],arr[i]])
    return print(result)

minimumAbsDifference([4,2,1,3])

#%%
#using zip

def minimumAbsDifference_2(arr):
    arr.sort() #sort the array first

    min_dif = min (b-a for a,b in zip(arr, arr[1:])) #find the min difference

    return print([[a,b] for a,b in zip(arr, arr[1:]) if b-a == min_dif]) #add to the list of list

minimumAbsDifference_2([4,2,1,3])
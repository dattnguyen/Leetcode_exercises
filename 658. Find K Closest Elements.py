# Given a sorted array arr, two integers k and x, find the k closest elements to x
# in the array. The result should also be sorted in ascending order.
# If there is a tie, the smaller elements are always preferred.


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

#%%
arr = [0,1,1,1,2,3,6,7,8,9]
k = 9
x = 4
diff = {}
res = []
for num in arr:
    diff[num] = abs(x-num)

sorted_map = {k: v for k, v in sorted(diff.items(), key=lambda item: item[1])}

print(sorted_map)
for key, v in enumerate(sorted_map):
    while v > 0:
        res.append(key)
        v -= 1
        k -=1
print(res)
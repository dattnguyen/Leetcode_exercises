# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if
# the number of different integers in that subarray is exactly K.
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
# Return the number of good subarrays of A.



#NOT DONE

from collections import Counter

A = [1,2,1,2,3]

k = 2
temp = k
res = 0

for left in range(len(A)):
    hmap = Counter()
    for right in range(left,len(A)):

        if A[right] not in hmap:
            hmap[A[right]] = 1
            k -= 1
        else:
            hmap[A[right]] += 1

        while len(hmap) == temp:
            res += 1
            hmap[A[left]] -= 1
            if hmap[A[left]] == 0:
                del hmap[A[left]]
                k += 1
            left += 1
print(res)

#%%
A = [1,2,1,3,4]
hmap = Counter()
k = 3
left = 0
res = 0

for i in A:
    hmap[i] = hmap.get(i,0) + 1

hmap[2] -= 1
if hmap[2] == 0:
    del hmap[2]

print(len(hmap))
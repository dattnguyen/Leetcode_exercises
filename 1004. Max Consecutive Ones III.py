# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# Return the length of the longest (contiguous) subarray that contains only 1s.

#two pointer technique. The idea is that as the right pointer sees a 0, we decrease K
#when K is less than 0, we want to move the left pointer toward, to create a window that
#holds the maximum 1s with k numbers of 0 in it
def longestOnes (A, K):
    left = 0
    for right in range(len(A)):
        if A[right] == 0: #if we see a 0, we decrease K
            K -= 1
        if K < 0:
            if A[left] == 0: #if the left pointer is at a 0, we increase K
                K += 1 #because when left move forward, the # of 0 will be decrease by 1
            left += 1 #if K is less than 0, increase left pointer

    return print(right - left + 1)

A = [1,1,1,0,0,0,0,0]
K = 2
longestOnes(A, K)

#%%
#normal way to do it with a counter to keep track of the max. In this situation, the counter
#is not necessary because the current window has the biggest length as it expands
A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3

left = 0
right = 0
counter = 0

for right in range(len(A)):
    if A[right] == 0:
        K -= 1

    if K < 0:
        if A[left] == 0:
            K += 1
        left += 1
        counter = max (counter, right - left +1)

print(counter)
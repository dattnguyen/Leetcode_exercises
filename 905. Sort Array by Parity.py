# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

#intuition: 2 pointer, everything left of even needs to be left
#everything right of odd needs to be odd
def sortArray(A):
    even = 0
    odd = len(A)-1
    while even < odd:
        while A[even] % 2 != 0 and even < odd:
            A[even], A[odd] = A[odd], A[even]
            odd -= 1
        even += 1
    return print(A)

sortArray([1,3])
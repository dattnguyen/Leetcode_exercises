# Given a non-empty array of integers, return the third maximum number in this array.
# If it does not exist, return the maximum number. The time complexity must be in O(n).
import math

def thirdMax (nums):

    first = -math.inf #keep track of the first, second, and third largest elements
    second = -math.inf
    third = -math.inf

    for i in nums:
        if i > first: #if it's greater than the current 1st max, we update the three variables
            third = second
            second = first
            first = i
        elif i > second and i < first:
            third = second
            second = i
        elif i > third and i < second:
            third = i
    if third != -math.inf:
        return print(third)
    else:
        return print(first)

thirdMax([1,2,2,5,3,5])
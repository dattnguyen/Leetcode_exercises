# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.

#intuition is that we record the sum of squared digits in a hashmap
#if we see the numbers again, we're going to end up in a cycle
#which means the number is not a happy number
def isHappy(n):
    seen = {} #hashmap to store squared digit

    while n != 1: #keep looping until we see the sum == 1 or we break
        cur = n #we need a variable to perform because n changes after every while loop
        nsum = 0
        while cur != 0: #use mod and floor divide to update the sum
            nsum += (cur % 10) ** 2
            cur //= 10

        if nsum in seen: #if we see the sum that means it's not happy
            return print(False)

        seen[nsum] = 1 #otherwise we add the sum to the seen hashmap

        n = nsum
    return print(True)

isHappy(19)
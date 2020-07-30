# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.

def isPerfectSquare(num):
    low = 0
    high = num
    if num == 1:
        return True
    while low <= high:
        mid = (low+high)//2
        if mid**2 == num:
            return True
        elif mid**2 > num:
            high = mid - 1
        else:
            low = mid + 1
    return False

#%%
#binary recursion
def isPerfectSquare_recursion(num):
    def helper(num, low, high):
        mid = (low + high) // 2
        if low > high:
            return False

        if mid ** 2 == num:
            return True
        elif mid ** 2 < num:
            return helper(num, mid + 1, high)
        else:
            return helper(num, low, mid - 1)

    return helper(num, 0, num)
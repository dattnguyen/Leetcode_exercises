# Given an integer, write a function to determine if it is a power of two.

def isPowerOfTwo_iterative(n):
    # if n == 0:
    #     return print('False')
    while n>0 and n%2 == 0:
        n //= 2
    if n == 1:
        return print('True')
    else:
        return print('False')

isPowerOfTwo_iterative(0)

#%%
def isPowerofTwo_recursive(n):
    if n == 0:
        return print('False')
    if n == 2 or n == 1:
        return print('True')
    elif n>2:
        return isPowerofTwo_recursive(n/2)
    else:
        return print('False')

isPowerofTwo_recursive(9)

#%%
def isPowerofTwo_bit(n):
    return n > 0 and not (n & n-1)

#n & n - 1 removes the left most bit of n.
# If an integer is power of 2, there is a single bit in the binary representation of n
# e.g. 16 = b10000, 16 - 1 = b01111, and 16 & 16 - 1 = b10000 & b01111 = 0
# also 16 != 0, based on these facts there is only one bit in b10000
# so 16 is power of 2.
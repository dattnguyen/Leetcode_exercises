# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

def isPowerofFour_recursion(num):
    if num == 4:
        return print('True')

    elif num > 4:
        return isPowerofFour_recursion(num/2)

    else:
        return print('False')

isPowerofFour_recursion(1)

#%%
def isPowerofFour_while(num):
    while num > 0 and num % 4 == 0:
        num //= 4

    if num == 1:
        return print('True')
    else:
        return print('False')

isPowerofFour_while(16)
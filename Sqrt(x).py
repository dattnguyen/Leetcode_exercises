#Implement int sqrt(int x).

def mySqrt(x):
    right = int(x/2) #binary search, upper bound is half of x
    left = 0 #lower bound is 0
    if x == 0: #special case
        return print(0)
    if x == 1: #special case
        return print(1)
    while left <= right:
        mid = int((left+right)/2) #binary search, middle point = 1/2(upper + lower)
        if mid**2 <= x < (mid+1)**2: #they ask for the integer so we need this condition
            return print(mid)
        elif mid**2 > x: # mid is greater than the sqrt, we need to reduce the upper bound
            right = mid - 1
        else: #and vice versa
            left = mid + 1
    return print(mid)

mySqrt(4)
#%%
import numpy as np
x = np.sqrt(8)
print (x)
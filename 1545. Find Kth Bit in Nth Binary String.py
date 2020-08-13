# Given two positive integers n and k, the binary string  Sn is formed as follows:
#
# S1 = "0"
# Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x,
# and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
#
# For example, the first 4 strings in the above sequence are:
#
# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

#intuition is the array is chopped into 3 parts. If k is at middle, it will be 1
#if k is on the left side, we do it recursively without changing the array
#if k is on the right side, we invert, and then revert before recursion

def findKthBit (n,k):
    if n == 1: #base case
        return '0'
    l = 2**n - 1 #length of string
    mid = l//2 + 1 #calculate the midpoint
    if k == mid: #if it's the midpoint, return 1
        return '1'
    elif k < mid:
        return findKthBit(n-1,k) #if it's on the left side, recursion on n-1
    else:
        return str(1-int(findKthBit(n-1,l-k+1)))

    #why l-k+1? Example: S(4) = 01110011011 '0' 001, k = 12
    # S(3) = 0111001 -> invert to 100 '0' 110
    #the number '0', which is the 12th element in S(4), is the (15-12+1) = 4th
    #element in the invert version of S(3)
    #after that, we take 1 - int(...) to find the reversed version

findKthBit(4,11)
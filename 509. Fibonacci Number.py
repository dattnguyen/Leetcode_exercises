# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

#dynamic programing
def fib(N):
    hmap = {0:0, 1:1}
    for i in range(2,N+1):
        hmap[i] = hmap[i-1] + hmap[i-2]

    return print(hmap[N])

fib(10)

#%%
#recursion

def fib2(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return fib2(N-1) + fib2(N-2)

fib2(5)

#%%
#recursion with memorization

def fib3(N):
    hmap = {0: 0, 1: 1} #create a hashmap to remember the elements that calculated
                        #because we want hashmap to be accessed globally,
                        #we need a helper function with the hashmap as a parameter
    def helper(hmap, N):

        if N == 0: #base case
            return hmap[0]
        elif N == 1: #base case
            return hmap[1]

        if N not in hmap: #if the element is not in hashmap, we add them to the map with the recursion relation
            hmap[N] = helper(hmap, N - 1) + helper(hmap, N - 2)
        return hmap[N]

    return helper(hmap, N)
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
# which sum to n.

#DP
#intuition: a number n can be written as (n - i*i + i*i) where i*i is a perfect square number
#the problem become find the number of perfect squares for (n-i*i) and add 1 to result
#we create a DP array to solve this
#O(N log(N)) - the first for loop is O(n). the second for loop is O(logN)
import math
def numSquares_dp(n):
    dp = [0] + [math.inf]*n #create a dp array with size n+1 as a placeholder
                            #because we need to account for 0
    if n < 0:
        return print(0)
    for i in range(1, n+1): #because we have number 0 in there so we need to start from 1, and +1 to the range
        dp[i] = min(dp[i - j**2] + 1 for j in range(1, int(math.sqrt(n))+1))
        #we need plus one here because if n = 13, we want to find j
        #in the range (1,4), sqrt(13) = 3.6, take the integer part +1

    return print(dp[n])

numSquares_dp(12)

#%%
#BFS
#                                      12
#               /                       |               \
#         11(12-1)                   8(12-4)          3(12-9)
#    /        |      \           /             \           \
#10(11-1)  7(11-4)  2(11-9)   7(8-1)          4(8-4)       2(3-1)
#                             /     \         /    \          \
#                          6(7-1)  3(7-4)  3(4-1)  0(4-4)    1(2-1)
#each node is calculated as the previous node subtract a perfect square number
#we need to find the shortest path that has leaf node '0'

from collections import deque
def numSquares_bfs(n):
    res = 0
    q = deque([n])
    while q:
        res += 1

        for i in range(len(q)):
            cur = q.popleft()
            for j in range(1, int(cur**0.5)+1):
                if cur - j**2 == 0:
                    return print(res)
                else:
                    q.append(cur-j**2)

    return print(res)

numSquares_bfs(13)

#%%
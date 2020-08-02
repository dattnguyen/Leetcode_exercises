# Given an integer array arr of distinct integers and an integer k.
#
# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]).
# In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0
# and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
#
# Return the integer which will win the game.
#
# It is guaranteed that there will be a winner of the game.

def getWinner(arr, k):
    count = k
    winner = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > winner:
            winner = arr[i]
            count = k
        count -= 1
        if count == 0:
            return print(winner)
    return print(winner)

getWinner([2,1,3,5,4,6,7], 2)
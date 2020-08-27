# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
# Return that maximum distance to closest person.

def maxDistToClosest(seats):
    # intuition is: we keep track of the last index where a seat it not empty
    # once we see a non-empty seat again, we update the result

    res = 0
    last = -1  # in the case there is no occupied seat at the beginning of the array [0,0,0,0,1]

    for i in range(len(seats)):
        if seats[i] == 1:  # if we see an occupied seat, update the res
            res = max(res, i if last == -1 else int(
                (i - last) / 2))  # update the seat [0,1,0,0,0,0,1], last = 2, i = 7, res = 2
            last = i  # update the index of the occupied seat

    # corner case, no occupied seat at the end [0,1,0,0,0,0,0] len(seats) = 7, last = 1, res = 7-1-1 = 5
    return print(max(res, len(seats) - last - 1))

maxDistToClosest([1,0,0,0,1,0,1])
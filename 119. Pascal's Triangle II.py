# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.

#the intuition is that if we are at row [1,2,1]
#we can add [0,1,2,1] with [1,2,1,0] to get [1,3,3,1] which is the next row
#use zip to make it pythonic
def getRow(rowIndex):
    row = [1]
    for i in range(rowIndex):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return print(row)

getRow(5)
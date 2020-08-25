# Given a collection of intervals, find the minimum number of intervals
# you need to remove to make the rest of the intervals non-overlapping.

import heapq
import math

#to revisit
def eraseOverlapIntervals(intervals):
    heap = [(x[1], x[0]) for x in intervals]

    heapq.heapify(heap)
    end = -math.inf
    res = 0

    while len(heap) > 0:
        cur = heapq.heappop(heap)
        if cur[1] >= end:
            end = cur[0]
        else:
            res += 1
    return print(res)

eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
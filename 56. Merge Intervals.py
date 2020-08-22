# Given a collection of intervals, merge all overlapping intervals.

#intuition is: first, we need to sort the interval
#when compared 2 intervals, if the second index of the first interval
#is greater than the first index of the second interval => overlapping
#we can update the second index of the first interval to be the max of the two
#we don't need to update the first index because we already sorted it, so
#the first index of the first interval will always be less than or equal to...

def merge(intervals):

    if len(intervals) == 0: #corner cases
        return print([])

    interval.sort()

    #can also use intervals.sort(key=lambda x: x[0])

    stack = [intervals[0]] #use a stack so we don't have to delete the second interval once
                            #we finish updating
    for interval in intervals[1:]:
        if interval[0] <= stack[-1][1]: #if the first index of the second interval
                                        #is <= the second index of the first interval
                                        #in this case the 'first interval' is the last
                                        #interval in our stack
            # update the second index of the last element of the stack
            stack[-1][1] = max(interval[1], stack[-1][1])
        else:
            stack.append(interval)

    return print(stack)

merge([[1,3],[2,6],[8,10],[15,18], [3,7]])
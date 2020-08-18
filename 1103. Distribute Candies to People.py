# We distribute some number of candies, to a row of n = num_people people in the following way:
# We then give 1 candy to the first person, 2 candies to the second person, and so on until
# we give n candies to the last person.
# Then, we go back to the start of the row, giving n + 1 candies to the first person,
# n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.
# This process repeats (with us giving one more candy each time, and moving to the start of the row
# after we reach the end) until we run out of candies.  The last person will receive all of
# our remaining candies (not necessarily one more than the previous gift).
# Return an array (of length num_people and sum candies) that represents the final distribution of candies.

#intuition: after the first distribution, the number of candies for index[0]
#would be the current candies for index[0] + number of people
def distributeCandies(candies: int, num: int):
    res = [0] * num
    distributed = 0
    level = 0
    while distributed < candies:
        for i in range(num):

            if distributed + num * level + i + 1 <= candies:
                res[i] = res[i] + num * level + i + 1
                distributed += num * level + i + 1
            else:
                res[i] = res[i] + candies - distributed
                return print(res)
        level += 1
    return print(res)

distributeCandies(124,7)

#%%
# Complexity
# Time O(sqrt(candies))
# Space O(N) for result
#
# The number of given candies is i + 1, which is an increasing sequence.
# The total number distributed candies is c * (c + 1) / 2 until it's bigger than candies.
# So the time it takes is O(sqrt(candies))

#we can use mode to make it easier...

def distribute(candies,n):
    res = [0] * n
    i = 0
    while candies > 0:
        res[i % n] += min(candies, i+1)
        candies -= i + 1
        i += 1
    return print(res)

distribute(124,6)
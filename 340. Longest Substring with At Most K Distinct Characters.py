# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# For example, Given s = “eceba” and k = 2,
#
# T is "ece" which its length is 3.

def findLongest(A, k):
    counter = Counter()
    left = res = 0
    for right in range(len(A)):
        if counter[A[right]] == 0: #if the character is not in there
            k -= 1 #reduce k by 1, we find the 1 distinct character
        counter[A[right]] += 1 #otherwise, we increase character's frequency
        while k < 0: #when we violate the condition
            counter[A[left]] -= 1 #we're going to move left pointer, but first
                                #we need to update its frequency in the map
            if counter[A[left]] == 0: #if we reduce the frequency to 0, meaning
                                #the character is not in the substring anymore
                k += 1 #we increase k, because we now have more distinct character to find
            left += 1 #move the left pointer
        res = max(res, right - left + 1)
    return print(res)
findLongest('eceba', 2)
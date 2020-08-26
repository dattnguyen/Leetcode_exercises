# Given a string and a string dictionary, find the longest string in the dictionary
# that can be formed by deleting some characters of the given string.
# If there are more than one possible results, return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.
import heapq
def findLongestWord(s,d):
    # sort the dict by word length and then alphabetically so the first valid word can be return immediately
    # by using a heap

    # create a heap/array that has tuples of (-length of word and word) because min heap
    heap = [(-len(word), word) for word in d]
    heapq.heapify(heap)

    while heap:
        word = heapq.heappop(heap)[1]  # we want to pop the word out, remember we put in the heap (tuples)

        # find the needle in the haystack:
        # check if the word can be formed from the string
        # 2 pointer technique:
        i = 0
        for j in range(len(s)):
            if i < len(word) and s[j] == word[i]:
                # we need to check if i < len(word) first, before we check the character.
                # E.g. in 'ale', i will be 3, and word[i] would be out of index
                i += 1
        if i == len(word):
            return print(word)

    return print('')

findLongestWord('abpcplea',["ale","apple","monkey","plea"])
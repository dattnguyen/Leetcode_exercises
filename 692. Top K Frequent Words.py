# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower alphabetical order comes first.

#intuition is: use a min heap to store the words and its frequency
#use -freq because in Python, heap is a default min heap
#in the tuple we have (-freq, word) because we want to sort by the frequency first
#then sort the word alphabetically
#we then pop the first word in heap out, and take the index[1] or the word
#in the tuple (-freq, word)

from collections import Counter
import heapq
def topKFrequent(words, k):
    count = Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return print([heapq.heappop(heap)[1] for i in range(k)])

topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
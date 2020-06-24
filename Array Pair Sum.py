#this is a similar problem to LeetCode two sum

# Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.
# So the input:
# pair_sum([1,3,2,2],4)
# would return 2 pairs:
#  (1,3)
#  (2,2)

arr = [2, 1, 4, 7, 5, 3]
k = 9
counter = []
result = []
for x in arr:
    if k-x not in counter:
        counter.append(x)
    else:
        result.append(x)
        result.append(k-x)
print(result)

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne(digits):
    nums = 0
    j = len(digits) - 1
    for i in range(len(digits)): #we need to convert the string to number
        nums += digits[i] * (10 ** j) #as the index position increase, the power need to decrease
        j -= 1
    nums = str(nums + 1) #and then convert to string so we can slide and add back to the new list
    newdigits = [x for x in nums]

plusOne([4,3,2,1])
#%%
def plusOne(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, (len(digits)-1-i)) #a more succint way to do it
    return [int(i) for i in str(num+1)]

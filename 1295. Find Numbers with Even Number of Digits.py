#Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
    even = 0
    for i in nums:
        counter = 0
        while i > 0:
            i = int(i / 10) #how many times you can divide a number by 10 before it hits
            counter += 1
        if counter !=0 and counter % 2 == 0: #the number of times you divide by 10 = the number of digits
            even += 1
    return print(even)

findNumbers([199,20,1,12])
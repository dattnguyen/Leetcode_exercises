# Given an array nums of n integers where n > 1,  return an array output such that
# output[i] is equal to the product of all the elements of nums except nums[i].

#the intuition is that when you go forward, you can't see the elements ahead, but
#you can see the elements behind, the ones you already pass
#so we go forward and calculate the sum product of everything to the left of current index
#and then go backward and do the same thing. The sum of the 2 arrays will be our result
nums = [5,4,3,2]

product = 1 #use product to keep track of the sum product as we move

result = []

for i in range(len(nums)): #first pass, going forward
    result.append(product) #sum product of everything to the left of the pointer
    product *= nums[i]

product = 1 #reset the sum product counter
for i in range(len(nums)-1, -1, -1): #going backward
    result[i] *= product
    p *= nums[i]

#%%

#using 2 pointers, same idea but 1 for loop

nums = [4,3,2,2]
result =[1] * len(nums)

left = 1
right = 1

for i in range(len(nums)):
    result[i] *= left #first pass, going forward
    left *= nums[i]

    result[-1 - i] *= right #second pass, going backward
    right *= nums[-1-i]

print(result)
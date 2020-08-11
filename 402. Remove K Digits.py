
def removedKDigit(num, k):
    stack = []
    #the intuition is that if you want to go from left to right
    #if you see the next digit is smaller than the current one
    #we remove the current digit to make the number smaller
    #we can use stack to pop the previous number
    for i in range(len(num)):

        while len(stack) > 0 and k > 0 and stack[-1] > num[i]:
            stack.pop()
            k -= 1
        stack.append(num[i])

    if k > 0: #in the case that the digits keep increasing '123456'
        stack = stack[:-k] #we can't pop anything out using the function above
                            #we then need to pop the last k elements, since we already
                            #know that the numbers are increasing

    # return print(stack)
    print(''.join(stack).lstrip('0') or '0') #you need or '0' in case stack is empty

removedKDigit('10',2)
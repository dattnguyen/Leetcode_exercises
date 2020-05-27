def is_palindrome(num):
    if num>=0:
        mylist = [int(d) for d in str(num)]
        rlist = mylist[::-1]
        if mylist == rlist:
            print(f'{num} is a palindrome number.')
        else:
            print(f'{num} is not a palindrome number.')
    else:
        print(f'{num} is not a palindrome number.')

is_palindrome(0)

#%% without turning into string
def is_palindrome(num):
    if num>=0:
        org = num
        reverse = 0
        while num!=0:
            reverse = reverse*10 + num % 10 #using mode to find the last digit
            num = int(num/10) #remove the last digit from the original number and do it again, until original number is 0
        if reverse == org:
            print(f'{org} is a palindrome number.')
        else:
            print(f'{org} is not a palindrome number.')
    else:
        print(f'{num} is not a palindrome number.')

is_palindrome(3434554343)



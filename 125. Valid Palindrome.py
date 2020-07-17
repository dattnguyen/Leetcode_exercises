# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

def isPalindrome(s):
    str = []
    for char in s: #split the string into alphanumeric characters and put in a string to process
        if char.isalnum() == True:
            str.append(char.lower())

    if not s:
        return print('True')
    head = 0 #using 2 pointer technique to check if palindrome
    tail = len(str) - 1
    while head < tail:
        if str[head] != str[tail]:
            return print('False')
        else:
            head += 1
            tail -=1
    return print('True')

isPalindrome('')
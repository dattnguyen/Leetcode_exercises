# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.

def validpalindrome(s):
    # intuition is if we see a pair that is mismatch, we want to run 2 check
    # one is to remove the character at the left pointer and check if the res is palindrome
    # two is to remove the character at the left pointer
    # something like a****b. We remove a and check if ****b is palindrome and vice versa
    def isPalindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return isPalindrome(s, left + 1, right) or isPalindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True


validpalindrome('abca')
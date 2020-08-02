# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

def detectCapitalUse(word):
    if len(word) == 1:
        return True

    if word[0].isupper() and word[1].isupper():
        for i in range(2, len(word)):
            if not word[i].isupper():
                return False

    else:
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
    return True

detectCapitalUse('LeetCode')
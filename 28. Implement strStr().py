#Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if needle == '':
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        # we don't need to check the last j character of the haystack. Plus 1 account for range function
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:  # check each character in haystack, move on to the next character if mismatch
                break
            if j == (len(needle) - 1):  # check if match the number of character of the needle
                return i
    return -1

strStr('hello', 'll')

#%%
#KMP method
def strStr2(haystack, needle):

    def kmp(str_):
        b, prefix = 0, [0]
        for i in range(1, len(str_)):
            while b > 0 and str_[i] != str_[b]:
                b = prefix[b - 1]
            if str_[b] == str_[i]:
                b += 1
            else:
                b = 0
            prefix.append(b)
        return prefix

    str_ = kmp(needle + '#' + haystack)
    n = len(needle)
    if n == 0:
        return n
    for i in range(n + 1, len(str_)):
        if str_[i] == n:
            return i - 2 * n
    return -1



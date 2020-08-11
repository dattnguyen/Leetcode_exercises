s = 'XY'
right = len(s)-1
mul = 0
res = 0
# hmap = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
#         'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
#         'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
#         'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
#         'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

while right >=0:
    res += (ord(s[right])-65+1) * (26**mul)
    right -= 1
    mul += 1

print(res)
#%%
print(ord('A')-65+1)
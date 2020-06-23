st = 'XCIV'

roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} # make a map for easy look up
sum = 0

for i in range(0,len(st)-1):
    if roman[st[i]] < roman[st[i+1]]: #if the letter with lower value is in the previous position, then we subtract it
        sum -= roman[st[i]]
    else:
        sum += roman[st[i]]
sum += roman[st[-1]] #we need to account for the last character
print(sum)


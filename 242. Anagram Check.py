# create a hashmap to check whether all the keys have 0 value by going through
#the first string and add all the char in, then go through the second string
#and decrease the value of the char
s1 = 'public relations'
s2 = 'crap built on lies'

s1 = s1.lower().replace(' ', '') # all lower case and remove space
s2 = s2.lower().replace(' ', '')

if len(s1) != len(s2): #length of two words has to be the same
    print('Not Anagram')

mydict = {} #create a dictionary to count each character

for char in s1:
    if char not in mydict:
        mydict[char] = 1 #if character is not in the dictionary, add it in
    else:
        mydict[char] += 1 #if character is in the dictionary, increase the count

for char in s2:
    if char not in mydict:
        mydict[char] = 1
    else:
        mydict[char] -= 1 #decrease the count

for k in mydict: #check if dictionary count is 0
    if mydict[k] != 0:
        print('Not Anagram')

#%%
#sort the string and add it to hmap, check whether if the 2 strings
#have the same sorted value

def isAnagram (s1, s2):
    hmap = {}
    key1 = ''.join(sorted(s1))
    key2 = ''.join(sorted(s2))
    hmap[key1] = 1
    if key2 in hmap:
        return print ('Two strings are anagram.')
    else:
        return print ('Two strings are NOT anagram.')

s1 = 'abc'
s2 = 'cba'

isAnagram(s1, s2)
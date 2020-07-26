import collections
s = 'codeleet'

indices = [4,5,6,7,0,2,1,3]

result = []
hmap = {}

for char, i in zip(s, indices):
    hmap[i] = char

od = collections.OrderedDict(sorted(hmap.items()))
for k, v in od.items():
    result.append(v)

print(''.join(result))

#%%
s = 'codeleet'
indices = [4,5,6,7,0,2,1,3]

N = len(s)
A = [0] * N
for ix, c in zip(indices, s):
    A[ix] = c
print (A)
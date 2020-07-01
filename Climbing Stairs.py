#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps.
#In how many distinct ways can you climb to the top?

def climbstairs(n):
    if n == 0:
        return print(0)
    if n == 1:
        return print(1)
    hmap = {0 : 1, 1: 1}
    for i in range(2,n+1):
        hmap[i] = hmap[i-1] + hmap[i-2]
    return print(hmap[n])

climbstairs(12)
#%%
n = 4
hmap = {0 : 1, 1: 1}
for i in range(2, n+1):
    hmap[i] = hmap[i - 1] + hmap[i - 2]
print(hmap[n])
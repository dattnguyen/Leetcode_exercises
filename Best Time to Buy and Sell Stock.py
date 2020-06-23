y = [7,1,3,6,3,7,9,0]
mylist = []
for i in range(0, len(y)):
    for j in range(0, len(y[i:])):
        if y[i] - y[i+j] < 0:
            mylist.append(y[i] - y[i+j])
print(-min(mylist))
#%%
y = [7,1,3,6,3,7,9,0]
minp = y[0]
mprofit = 0

for i in y:
    minp = min (minp, i) #find the lower of the 2 values, set the new min
    profit = i - minp #calculate the profit, could be negative value if stock goes down
    mprofit = max(mprofit, profit) #if the stock goes down, ignore and move on
print(mprofit)

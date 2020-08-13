# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

#DFS
#the intuition is that when you search for an island
#when you see an island or cell '1', you DFS for the 4 directions,
#or 4 cells around '1'. In your DFS, you 'mark' the cell you visited
#by changing it from '1' to '0'. We also increase the count because
#we know it's an island

def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
        #the first 4 conditions is to check if we go outside the grid, or if we see water ('!=1')
        #then we return or do nothing
    grid[i][j] = '#'  #otherwise we mark the cell (island or '1') as '0'
        #and then perform dfs on the 4 cells around it

    dfs(grid, i + 1, j)  # cell above
    dfs(grid, i - 1, j)  # cell below
    dfs(grid, i, j + 1)  # cell left
    dfs(grid, i, j - 1)  # cell right

def numIslands(grid):
    if not grid: #in case the grid is empty
        return 0

    count = 0

    for i in range(len(grid)): #go by row
        for j in range(len(grid[0])): #then go by each index of the row, or column
            if grid[i][j] == '1': #if we see an island
                dfs(grid,i,j) #we perform dfs, or look at 4 cells around it
                count += 1 #we now found one island
    return print(count)

numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
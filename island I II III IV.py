
'''
Find DFS all path
'''
def findAllPath(graph, start, end):
    def dfs(start, end, path = None):
        if path is None:
            path = []
        path.append(start)
        if start == end:
            res.append(path)
        else:
            for nb in graph[start]:
                if nb not in set(path):
                    dfs(nb, end, path[:])
    res = []
    dfs(start, end)
    return res

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(findAllPath(graph, 'A', 'F'))


'''
Given a 2D array as a geographical map where 1 is land and 0 is ocean, write a function to compute the number of isalnds on this geographical map.

For example, input as follows:
11000
11000
00100
00011

Output shall be: 3
'''
def numIsland(grid):
    def dfs(r, c, rows, cols):
        if 0 <= r < rows and 0<= c < cols and grid[r][c] == '1':
            grid[r][c] = '#'
            for d in dirs:
                dfs(r + d[0], c + d[1], rows, cols)
    rows = len(grid)
    cols = len(grid[0])
    dirs = [[0,1], [1,0], [-1, 0], [0,-1]]
    res = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j, rows, cols)
                res += 1
    return res

print(numIsland([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

'''  
Follow up:
max area
'''
def numIslands2(grid):
    def dfs(r, c, rows, colsr):
        if 0 <= r < rows and 0<= c < cols and grid[r][c] == '1':
            grid[r][c] = '#'
            sum = 1
            for d in dirs:
                sum += dfs(r + d[0], c + d[1], rows, cols)
            return sum
        return 0

    rows = len(grid)
    cols = len(grid[0])
    dirs = [[0,1], [1,0], [-1, 0], [0,-1]]
    res = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                res = max(res, dfs(i, j, rows, cols))
    return res

print(numIslands2([["1","0","1","1","0"],["0","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

'''
Follow up
perimeter

we can use the second solution, change the sum to calculate the total number of edge is 0
'''
def numIslands3(grid):
    def dfs(r, c, rows, cols):
        res = 0
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
            grid[r][c] = '#'
            res = 0
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1 or grid[nr][nc] =='0':
                    res += 1
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                res += dfs(nr, nc, rows, cols)
        return res
    rows = len(grid)
    cols = len(grid[0])
    dirs = [[0,1], [1,0], [-1, 0], [0,-1]]
    res = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                res = max(res, dfs(i, j, rows, cols))
    return res
print(numIslands3([['1','1'], ['1', '0'], ['1','1']]))
'''
Follow up

fiil water with land, make area maximum
'''





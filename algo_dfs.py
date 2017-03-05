def getNeighbors(grid, row_index, column_index):
    row_bound = len(grid)
    column_bound = len(grid[0])
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for neighbor in neighbors:
        row = row_index + neighbor[0]
        column = column_index + neighbor[1]
        if row >= 0 and column >= 0 and row < row_bound and column < column_bound:
            print(grid[row][column])
    

def getBiggestRegion(grid):
    for row_index, row in enumerate(grid):
        column_index = 0
        for column in row:
            print('Cell:', row_index, column_index)  
            getNeighbors(grid, row_index, column_index)
            column_index += 1

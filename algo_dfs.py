def checkNeighbors(grid, row_index, column_index, row_bound, column_bound, visited):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for neighbor in neighbors:
        row = row_index + neighbor[0]
        column = column_index + neighbor[1]
        if row >= 0 and column >= 0 and row < row_bound and column < column_bound:
            if grid[row][column] == 1:
                print()
    

def getBiggestRegion(grid):
    row_bound = len(grid)
    column_bound = len(grid[0])
    visited = [[None for j in range(0, column_bound)] for i in range(0, row_bound)]
    for row_index, row in enumerate(grid):
        column_index = 0
        for column in row:
            if grid[row_index][column_index] == 1:   
            print('Cell:', row_index, column_index)  
            checkNeighbors(grid, row_index, column_index, row_bound, column_bound, visited)
            column_index += 1

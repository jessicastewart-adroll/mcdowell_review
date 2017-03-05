def get_max_region(grid, row_index, column_index):
    print(row_index, column_index)
    row_bound = len(grid)
    column_bound = len(grid[0])
    if grid[row_index][column_index] == 0:
        return 0
    
    if row_index >= 0 and column_index >= 0 and row_index < row_bound and column_index < column_bound:
        return 0
    
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for neighbor in neighbors:
        row = row_index + neighbor[0]
        column = column_index + neighbor[1]
        # check bounds 
        if row >= 0 and column >= 0 and row < row_bound and column < column_bound:
            if grid[row][column] == 1:
                return 1 + get_max_region(grid, row, column)
    

def getBiggestRegion(grid):
    max_region = 0
    for row_index, row in enumerate(grid):
        column_index = 0
        for column in row:
            max_region = max(max_region, get_max_region(grid, row_index, column_index))
            return
            column_index += 1

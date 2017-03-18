### fourth try
def search(grid, row, column):
  if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]):
    return 0
    
  if not grid[row][column]:
    return 0
    
  grid[row][column] = 0  
  count = 1
  count += search(grid, row+1, column)
  count += search(grid, row, column+1)
  count += search(grid, row, column-1)
  count += search(grid, row-1, column)
  count += search(grid, row-1, column-1)
  count += search(grid, row+1, column+1)
  count += search(grid, row-1, column+1)
  count += search(grid, row+1, column-1)
  return count
    

def getBiggestRegion(grid):
  largest_region = 0
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      count = search(grid, row, column)
      largest_region = max(count, largest_region)
  return largest_region

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))


### third try
def largest_connected_component(board):
	largest_count = 0
	for row in range(len(board)):
		for column in range(len(board[0])):
			largest_count = max(largest_count, dfs(board, row, column))
	return largest_count			

def dfs(board, row, column):
	if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]):
		return 0

	if not board[row][column]:
		return 0
	else:	
		board[row][column] = 0
		count = 1
	
	neighbors = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
	for neighbor in neighbors:
		x = row + neighbor[0]
		y = column + neighbor[1]
		count += dfs(board, x, y)
	return count		

# TEST					
board = [
			[1, 1, 0, 0],
			[0, 1, 1, 0],
			[0, 0, 1, 0],
			[1, 0, 0, 0],
		]
print(largest_connected_component(board))

### second try
def largest_connected_component(board):
	largest_count = 0
	for row in range(len(board)):
		for column in range(len(board[0])):
			if board[row][column] == 1:
				board[row][column] = 0
				count = dfs(board, row, column, 1)
				largest_count = max(largest_count, count)
	return largest_count			

def dfs(board, row, column, count):
	neighbors = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
	for neighbor in neighbors:
		x = row + neighbor[0]
		y = column + neighbor[1]
		if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
			continue
		if board[x][y] == 1:
			board[row][column] = 0
			count += 1 
			count = dfs(board, x, y, count)
	return count		

# TEST					
board = [
			[1, 1, 0, 0],
			[0, 1, 1, 0],
			[0, 0, 1, 0],
			[1, 0, 0, 0],
		]
print(largest_connected_component(board))

### first try
def largest_connected_component(board):
	largest_count = 0
	for row in range(len(board)):
		for column in range(len(board[0])):
			if board[row][column] == 0:
				continue
			else:
				count = 1
				count += dfs(board, row+1, column)
				count += dfs(board, row-1, column)
				count += dfs(board, row, column+1)
				count += dfs(board, row, column-1)
				count += dfs(board, row+1, column+1)
				count += dfs(board, row-1, column-1)
				count += dfs(board, row+1, column-1)
				count += dfs(board, row-1, column+1)
				largest_count = max(largest_count, count)
	return largest_count			

def dfs(board, row, column):
	if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]):
		return 0
	if board[row][column] == 1:
		board[row][column] = 0
		count += 1
		count += dfs(board, row+1, column)
		count += dfs(board, row-1, column)
		count += dfs(board, row, column+1)
		count += dfs(board, row, column-1)
		count += dfs(board, row+1, column+1)
		count += dfs(board, row-1, column-1)
		count += dfs(board, row+1, column-1)
		count += dfs(board, row-1, column+1)
		return 1	
	else:
		return 0	
					
board = [
			[1, 1, 0, 0],
			[0, 1, 1, 0],
			[0, 0, 1, 0],
			[1, 0, 0, 0],
		]
print(largest_connected_component(board))
